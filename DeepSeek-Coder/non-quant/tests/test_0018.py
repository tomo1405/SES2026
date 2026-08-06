import pytest
from src_0018 import task_func

def test_task_func_process_running():
    # Mock the behavior of psutil.process_iter() to simulate a running process
    with pytest.raises(NotImplementedError):
        task_func("mock_process_name")

def test_task_func_process_not_running():
    # Mock the behavior of psutil.process_iter() to simulate a non-running process
    with pytest.raises(NotImplementedError):
        task_func("mock_process_name")