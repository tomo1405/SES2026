import pytest
from src_0364 import calculate_factorial, task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    expected_result = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    result = task_func(numbers)
    assert result == expected_result, "Task function returned an incorrect result"

def test_calculate_factorial():
    number = 5
    expected_result = 120
    result = calculate_factorial(number)
    assert result == expected_result, "Calculate factorial function returned an incorrect result"

def test_task_func_with_invalid_input():
    numbers = [1, 2, 3, '4', 5]
    with pytest.raises(ValueError):
        task_func(numbers)