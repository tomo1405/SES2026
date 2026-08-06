import re
import string
from random import choice
from src_0454 import task_func
import pytest

def test_task_func():
    n = 10
    pattern = r'[a-z]{3}[0-9]{3}'
    result = task_func(n, pattern)
    assert isinstance(result, str)
    assert len(result) == n
    assert re.match(pattern, result)

def test_task_func_with_invalid_pattern():
    n = 10
    pattern = r'[a-z]{3}[0-9]{4}'
    with pytest.raises(ValueError):
        task_func(n, pattern)