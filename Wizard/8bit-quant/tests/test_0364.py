python
import pytest
from src_0364 import calculate_factorial, task_func

def test_calculate_factorial():
    assert calculate_factorial(0) == (0, 1)
    assert calculate_factorial(1) == (1, 1)
    assert calculate_factorial(5) == (5, 120)
    assert calculate_factorial(10) == (10, 3628800)

def test_task_func():
    assert task_func([0, 1, 5, 10]) == {0: (0, 1), 1: (1, 1), 5: (5, 120), 10: (10, 3628800)}
    with pytest.raises(ValueError):
        task_func([0, 1, 5, '10'])