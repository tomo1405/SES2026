import pytest
from src_0246 import task_func

def test_task_func():
    result = task_func()
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert isinstance(result['mean'], (int, float))
    assert isinstance(result['mean'], (int, float))
    assert isinstance(result['median'], (int, float))
    assert isinstance(result['mode'], (int, float))