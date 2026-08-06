import pytest
from src_0454 import task_func

def test_task_func():
    n = 10
    pattern = r'[a-zA-Z0-9]{10}'
    result = task_func(n, pattern)
    assert re.match(pattern, result)