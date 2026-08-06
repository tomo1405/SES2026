from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import os
import re
import glob
import time
from decimal import Decimal, ROUND_HALF_UP
import datetime
import torch
import requests
import traceback

WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

def get_d_h_m_s(sec):
    td = datetime.timedelta(seconds=sec)
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    return td.days, h, m, s

def extract_code(response):
    code_pattern = r'```(?:(\w+)\n)?([\s\S]*?)```'
    content = re.search(code_pattern, response)
    try:
        return content.group(2).strip()
    except:
        print('Regeneration ...')
        return None
    
def notify(message):
    requests.post(
        WEBHOOK_URL,
        json={"text": message},
        timeout=10
    )

def main():
    model_name = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"

    target_dir = "../../src/"
    output_dir = "./tests/" # dst
    os.makedirs(output_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(target_dir, "*.py")))
    
    assert torch.cuda.is_available(), "GPU が利用できません。CUDA環境を確認してください。"
    print(f"使用GPU: {torch.cuda.get_device_name(0)}")

    bnb_config = BitsAndBytesConfig(
        load_in_8bit=True
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="cuda",
        quantization_config=bnb_config
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    open("./timeout.txt", 'w').close()

    before_allocated = []
    before_reserved  = []
    after_allocated = []
    after_reserved  = []
    
    start = time.time()

    for i, file in enumerate(files):
        timeout_st = time.time()
        ok = True
        print(f'Processing at: {(i + 1)} / {len(files)}')
        module_name = os.path.splitext(os.path.basename(file))[0]
        file_name = os.path.basename(file)
        input_path = f"{target_dir}/{file_name}"
        with open(input_path) as f:
            src_code = f.read()

        prompt = f'''
    Generate pytest unit tests for the function below.

    Rules:
    - Do not modify or rewrite the target code
    - Return ONLY valid Python code inside a single code block
    - Import explicitly: from {module_name} import <function>
    - Import pytest
    - Import other modules appropriately as well, if necessary

    Target code:
    ```python
    {src_code}
    ```
    '''

        messages = [
            {"role": "system", "content": "You are an expert Python testing engineer."},
            {"role": "user", "content": prompt}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
        
        before_allocated.append(torch.cuda.memory_allocated() / 1e9)
        before_reserved.append(torch.cuda.memory_reserved() / 1e9)
        
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=2048
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        
        # 生成前後を比較することで：
        # - ピーク時の使用量がわかる
        # - 入力コードが長いファイルほどメモリを多く消費するかどうか確認できる
        # - OOM（メモリ不足）が起きた場合の原因特定に役立つ
        # - `before_generate` と `after_generate` を比較することで、生成時のメモリ増加量がわかる
        # 生成前：モデルの重みのみ
        # 生成後：モデルの重み＋KVキャッシュ＋生成トークン
        # 記録が生成後だけでよい場合（モデルロード時の使用量だけ知りたいなど）は、before_generate の行を削除しても問題ありません。
        after_allocated.append(torch.cuda.memory_allocated() / 1e9)
        after_reserved.append(torch.cuda.memory_reserved() / 1e9)
        
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        generated_code = extract_code(response)

        while generated_code is None:
            if int(time.time() - timeout_st) >= 300:
                with open("./timeout.txt", 'a') as f:
                    f.write(file_name + '\n')
                ok = False
                break
            
            before_allocated.append(torch.cuda.memory_allocated() / 1e9)
            before_reserved.append(torch.cuda.memory_reserved() / 1e9)
            
            generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=2048
            )
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]
            
            after_allocated.append(torch.cuda.memory_allocated() / 1e9)
            after_reserved.append(torch.cuda.memory_reserved() / 1e9)
            
            response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            generated_code = extract_code(response)
        
        output_path = f"{output_dir}/test_{i + 1:04}.py"

        if ok:
            with open(output_path, 'w') as f:
                f.write(generated_code)
        
        total_time = time.time() - start
        total_sec = float(Decimal(str(total_time)).quantize(Decimal('0.001'), ROUND_HALF_UP))
        print(f'Total second: {total_sec}')
        time_avg = total_time / (i + 1)
        print(f'Average second: {time_avg} s / file')
        day, hour, minute, second = get_d_h_m_s(total_time)
        print(f"Total Time: {day} d {hour} h {minute} m {second} s")

        if i != len(files) - 1:
            print('-' * 100)
            
    with open("time_avg.txt", 'w') as f:
        f.write(str(time_avg))
    
    with open("time_total.txt", 'w') as f:
        f.write(str(total_time))

    before_allocated_avg = float(Decimal(str(sum(before_allocated) / len(before_allocated))).quantize(Decimal('0.001'), ROUND_HALF_UP))
    before_reserved_avg = float(Decimal(str(sum(before_reserved) / len(before_reserved))).quantize(Decimal('0.001'), ROUND_HALF_UP))
    after_allocated_avg = float(Decimal(str(sum(after_allocated) / len(after_allocated))).quantize(Decimal('0.001'), ROUND_HALF_UP))
    after_reserved_avg = float(Decimal(str(sum(after_reserved) / len(after_reserved))).quantize(Decimal('0.001'), ROUND_HALF_UP))
    
    # # どちらも「このPythonプロセス」のみの値
    # torch.cuda.memory_allocated()  # テンソルが実際に占有している量
    # torch.cuda.memory_reserved()   # PyTorchがOSから確保済みの量（キャッシュ含む）

    # allocated と reserved の違い

    # GPU物理メモリ
    # ├── reserved（PyTorchが確保済み）
    # │   ├── allocated（テンソルが実際に使用中）
    # │   └── キャッシュ（将来の割り当て用に保持）
    # └── 他プロセス・他ユーザーの領域（取得不可）

    # - allocated → 現在テンソルが占めている量（実態に近い）
    # - reserved → PyTorchがOSから確保している総量（allocated 以上になる）

    # 通常は allocated を記録すれば十分です。
    
    with open("before_allocated.txt", 'w') as f:
        f.write(str(before_allocated_avg))
        
    with open("before_reserved.txt", 'w') as f:
        f.write(str(before_reserved_avg))
        
    with open("after_allocated.txt", 'w') as f:
        f.write(str(after_allocated_avg))
        
    with open("after_reserved.txt", 'w') as f:
        f.write(str(after_reserved_avg))

    print("Completed!!")
    
if __name__ == "__main__":
    try:
        st = time.time()
        main()
        notify(
        f"DeepSeek(8bit)\n"
        f"✅ 処理完了しました\n"
        f"実行時間: {(time.time() - st) / 60:.1f} 分\n"
        )

    except Exception:
        notify(
            "❌ エラーが発生しました\n```"
            + traceback.format_exc()[-3000:]
            + "```"
        )
        raise