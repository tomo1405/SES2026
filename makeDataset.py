from datasets import load_dataset
import os

ds = load_dataset(
    "bigcode/bigcodebench",
    split="v0.1.4",
)

output_dir = "./src"
os.makedirs(output_dir, exist_ok=True)

for i, data in enumerate(ds):
    path = f"{output_dir}/src_{i + 1:04}.py"
    code_prompt = data["code_prompt"]
    canonical_solution = data["canonical_solution"]
    merged_code = code_prompt + canonical_solution

    with open(path, 'w') as f:
        f.write(merged_code)

print("Save completed")