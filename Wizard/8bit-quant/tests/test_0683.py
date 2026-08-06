python
import pytest
from src_0683 import task_func

def test_task_func():
    nested_dict = {
        'a': {'x': 1, 'y': 2},
        'b': {'x': 3, 'y': 4},
        'c': {'x': 5, 'y': 6},
    }
    expected_result = {'x': 0.8414709848078965, 'y': 0.9092974268256817}
    assert task_func(nested_dict) == expected_result