import pytest
from src_0277 import task_func

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    skewness, kurtosis, ax = task_func(matrix)
    
    assert skewness != 0
    assert kurtosis != 0
    assert ax is not None