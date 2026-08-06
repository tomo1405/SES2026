import pytest
from src_0116 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert result['array'].tolist() == numbers
    assert result['mode'] == 3
    assert result['entropy'] == 1.5849625007211563

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2, 3, 'a'])