import pytest
from src_1140 import task_func

def test_task_func():
    data = [
        {'Hours': 10, 'Scores': 80},
        {'Hours': 20, 'Scores': 90},
        {'Hours': 30, 'Scores': 70},
        {'Hours': 40, 'Scores': 60},
        {'Hours': 50, 'Scores': 50},
        {'Hours': 60, 'Scores': 40},
        {'Hours': 70, 'Scores': 30},
        {'Hours': 80, 'Scores': 20},
        {'Hours': 90, 'Scores': 10},
        {'Hours': 100, 'Scores': 0}
    ]
    expected_mse = 10.0
    actual_mse = task_func(data)
    assert actual_mse == expected_mse