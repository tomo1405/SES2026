import pytest
from src_0937 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func('hello123')
    with pytest.raises(ValueError):
        task_func('HELLO')
    assert task_func('hello') is not None