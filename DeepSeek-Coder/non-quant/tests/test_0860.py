import pytest
from src_0860 import task_func

def test_task_func():
    accuracy, warning_msg = task_func()
    assert accuracy >= 0.9, "Expected accuracy to be at least 0.9"
    assert warning_msg is None, "Expected no warning message"