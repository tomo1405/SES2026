import pytest
from src_0005 import task_func

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    expected_result = {'a': 3, 'b': 3, 'c': 3, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    assert task_func(d) == expected_result