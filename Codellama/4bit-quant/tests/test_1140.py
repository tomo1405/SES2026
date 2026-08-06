import pytest
from src_1140 import task_func

def test_task_func():
    data = {'Hours': [10, 20, 30, 40, 50], 'Scores': [80, 90, 100, 110, 120]}
    expected_mse = 1.0
    actual_mse = task_func(data)
    assert actual_mse == expected_mse