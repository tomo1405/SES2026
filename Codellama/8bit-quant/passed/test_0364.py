import pytest
from src_0364 import task_func

def test_task_func_with_valid_input():
    numbers = [1, 2, 3, 4, 5]
    expected_result = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    assert task_func(numbers) == expected_result

def test_task_func_with_invalid_input():
    numbers = [1, 2, 3, 4, "a"]
    with pytest.raises(ValueError):
        task_func(numbers)