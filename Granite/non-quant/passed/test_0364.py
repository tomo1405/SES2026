import pytest
from src_0364 import calculate_factorial, task_func

def test_calculate_factorial():
    assert calculate_factorial(0) == (0, 1)
    assert calculate_factorial(1) == (1, 1)
    assert calculate_factorial(5) == (5, 120)
    with pytest.raises(ValueError):
        calculate_factorial(-1)

def test_task_func():
    assert task_func([0, 1, 2, 3, 4]) == {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}
    with pytest.raises(ValueError):
        task_func([0, 1, 2, '3', 4])