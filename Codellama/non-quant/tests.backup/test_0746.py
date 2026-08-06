import pytest
from src_0746 import task_func

def test_task_func():
    script_path = task_func()
    assert script_path.endswith('.sh')
    assert os.path.isfile(script_path)
    assert os.access(script_path, os.X_OK)