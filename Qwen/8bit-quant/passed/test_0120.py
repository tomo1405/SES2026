import pytest
from src_0120 import task_func

def test_task_func():
    # Since the function primarily deals with plotting, we can't directly assert anything.
    # However, we can check if the function runs without raising any exceptions.
    try:
        task_func()
    except Exception as e:
        pytest.fail(f"task_func raised an exception: {e}")