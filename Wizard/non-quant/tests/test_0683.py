python
import pytest
from src_0683 import task_func

def test_task_func():
    nested_dict = {
        'a': {'x': 1, 'y': 2},
        'b': {'x': 3, 'y': 4, 'z': 5},
        'c': {'w': 6, 'x': 7, 'y': 8, 'z': 9}
    }
    expected_result = {'x': 0.8414709848078965, 'y': 0.9092974268256817, 'z': 0.1411200080598672}
    assert task_func(nested_dict) == expected_result