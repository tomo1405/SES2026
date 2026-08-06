import re
import string
from random import choice
from src_0454 import task_func
import pytest

def test_task_func():
    n = 10  # Example input value
    pattern = r'[a-z]{3}[0-9]{2}'  # Example input value
    result = task_func(n, pattern)
    assert isinstance(result, str)
    assert len(result) == n
    assert re.match(pattern, result)

def test_task_func_with_invalid_input():
    n = -1  # Example invalid input value
    pattern = r'[a-z]{3}[0-9]{2}'  # Example input value
    with pytest.raises(ValueError):
        task_func(n, pattern)