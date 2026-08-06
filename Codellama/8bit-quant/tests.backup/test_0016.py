import pytest
from src_0016 import task_func

def test_task_func_valid_input():
    commands_file_path = 'commands.csv'
    output_dir_path = 'output'
    output_files = task_func(commands_file_path, output_dir_path)
    assert len(output_files) == 3
    assert os.path.exists(output_files[0])
    assert os.path.exists(output_files[1])
    assert os.path.exists(output_files[2])

def test_task_func_invalid_input():
    commands_file_path = 'invalid_commands.csv'
    output_dir_path = 'output'
    with pytest.raises(FileNotFoundError):
        task_func(commands_file_path, output_dir_path)

def test_task_func_invalid_output_dir():
    commands_file_path = 'commands.csv'
    output_dir_path = 'invalid_output'
    with pytest.raises(FileNotFoundError):
        task_func(commands_file_path, output_dir_path)