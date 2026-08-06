import pytest
from src_0006 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, dict), "The result should be a dictionary."
    assert all(isinstance(k, str) and all(isinstance(v, float) for v in result.values()) for k, v in result.items()), "The dictionary values should be floats."
    assert all(0 <= v <= 100 for v in result.values()), "All values should be between 0 and 100."