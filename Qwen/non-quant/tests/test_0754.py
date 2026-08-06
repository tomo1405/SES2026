import pytest
from src_0754 import task_func
import math
import random
import statistics

def test_task_func_zero_iterations():
    with pytest.raises(ZeroDivisionError):
        task_func(0)

def test_task_func_one_iteration():
    random.seed(0)  # Ensure reproducibility
    result = task_func(1)
    assert result == 0.0

def test_task_func_multiple_iterations():
    random.seed(0)  # Ensure reproducibility
    result = task_func(10)
    expected_mean = 3.8986  # Pre-calculated expected mean for 10 iterations with seed 0
    assert math.isclose(result, expected_mean, rel_tol=1e-4)

def test_task_func_large_number_of_iterations():
    random.seed(0)  # Ensure reproducibility
    result = task_func(1000)
    expected_mean = 3.8979  # Pre-calculated expected mean for 1000 iterations with seed 0
    assert math.isclose(result, expected_mean, rel_tol=1e-4)

def test_task_func_negative_iterations():
    with pytest.raises(ValueError):
        task_func(-1)