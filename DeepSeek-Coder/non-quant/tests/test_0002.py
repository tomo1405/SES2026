import pytest
from src_0002 import task_func

def test_task_func_positive():
    result = task_func(10)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) == len(set(result)), "The result should contain unique characters"

def test_task_func_negative():
    with pytest.raises(ValueError):
        task_func(-1)