import pytest
from src_0347 import task_func

def test_task_func_script_exists():
    script_path = "test_script.py"
    with pytest.raises(ValueError):
        task_func(script_path)

def test_task_func_script_does_not_exist():
    script_path = "test_script.py"
    with pytest.raises(ValueError):
        task_func(script_path)

def test_task_func_script_raises_exception():
    script_path = "test_script.py"
    with pytest.raises(subprocess.CalledProcessError):
        task_func(script_path)

def test_task_func_script_does_not_raise_exception():
    script_path = "test_script.py"
    task_func(script_path)

def test_task_func_script_with_args():
    script_path = "test_script.py"
    args = ["arg1", "arg2"]
    task_func(script_path, *args)

def test_task_func_script_with_wait():
    script_path = "test_script.py"
    task_func(script_path, wait=True)

def test_task_func_script_with_no_wait():
    script_path = "test_script.py"
    task_func(script_path, wait=False)