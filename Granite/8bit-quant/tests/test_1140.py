import pytest
from src_1140 import task_func

def test_task_func():
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected_mse = 1.0
    
    actual_mse = task_func(data)
    
    assert actual_mse == expected_mse