import pytest
from src_1140 import task_func

def test_task_func():
    data = {
        'Hours': [1, 2, 3, 4, 5],
        'Scores': [10, 20, 25, 40, 50]
    }
    result = task_func(data)
    assert isinstance(result, (int, float)), "The result should be a number"