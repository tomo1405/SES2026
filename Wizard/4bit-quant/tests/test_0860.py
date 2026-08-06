python
import pytest
from src_0860 import task_func

def test_task_func():
    accuracy, warning_msg = task_func()
    assert isinstance(accuracy, float)
    assert isinstance(warning_msg, str) or warning_msg is None