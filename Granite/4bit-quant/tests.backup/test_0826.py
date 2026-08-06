import pytest
from src_0826 import task_func
import numpy as np
import string

def test_task_func():
    # Test case 1: Default parameters
    result = task_func(length=3)
    assert isinstance(result, list)
    assert len(result) == 10
    for item in result:
        assert isinstance(item, str)
        assert len(item) == 3
    # Test case 2: Custom parameters
    result = task_func(length=5, seed=42, alphabets=list(string.ascii_uppercase))
    assert isinstance(result, list)
    assert len(result) == 10
    for item in result:
        assert isinstance(item, str)
        assert len(item) == 5
    # Test case 3: edge cases
    with pytest.raises(ValueError):
        task_func(length=0)
    with pytest.raises(ValueError):
        task_func(length=-1)
    with pytest.raises(TypeError):
        task_func(length=3, seed='abc')
    with pytest.raises(TypeError):
        task_func(length=3, alphabets=123)