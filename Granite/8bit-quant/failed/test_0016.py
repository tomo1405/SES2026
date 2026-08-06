import os
import pytest
from src_0016 import task_func

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv", "output_dir")

def test_task_func_output_dir_created():
    output_dir = "output_dir"
    if os.path.exists(output_dir):
        os.rmdir(output_dir)
    task_func("commands_file.csv", output_dir)
    assert os.path.exists(output_dir)
    os.rmdir(output_dir)

def test_task_func_commands_ executed():
    output_dir = "output_dir"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    commands_file_path = "commands_file.csv"
    with open(commands_file_path, "w") as f:
        f.write("command1\ncommand2\ncommand3")
    output_files = task_func(commands_file_path, output_dir)
    for output_file in output_files:
        with open(output_file, "r") as f:
            output = f.read()
        assert "Error executing command" not in output
    os.remove(commands_file_path)
    for output_file in output_files:
        os.remove(output_file)
    os.rmdir(output_dir)