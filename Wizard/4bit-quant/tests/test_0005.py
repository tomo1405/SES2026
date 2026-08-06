python
import pytest
from src_0005 import task_func

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
    expected_result = {'a': 3, 'b': 3, 'c': 3}
    assert task_func(d) == expected_result