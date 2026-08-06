import pytest
from src_0605 import task_func

def test_task_func_valid_filepath():
    filepath = 'test_file.cpp'
    task_func(filepath)
    assert subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])

def test_task_func_invalid_filepath():
    filepath = 'invalid_file.cpp'
    with pytest.raises(FileNotFoundError):
        task_func(filepath)

def test_task_func_compiler_error():
    filepath = 'test_file.cpp'
    with pytest.raises(subprocess.CalledProcessError):
        task_func(filepath)