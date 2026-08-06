import random
import string
import base64
import zlib
from src_0549 import task_func
import pytest

def test_task_func():
    # Test with default string length
    result = task_func()
    assert isinstance(result, str)
    assert len(result) == 100

    # Test with custom string length
    string_length = 50
    result = task_func(string_length)
    assert isinstance(result, str)
    assert len(result) == string_length

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid')