python
import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    try:
        shutil.copy(script_path, temp_dir)
        temp_script_path = os.path.join(temp_dir, os.path.basename(script_path))
        result = subprocess.call(["python", temp_script_path])
        print(result)
        if result == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return "Script execution failed!"

def test_task_func():
    script_path = "script.py"
    temp_dir = "temp_dir"
    os.mkdir(temp_dir)
    with open(script_path, "w") as f:
        f.write("print('Hello, World!')")
    assert task_func(script_path, temp_dir) == "Script executed successfully!"
    os.remove(script_path)
    os.rmdir(temp_dir)