import pytest
from src_0296 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    expected_result = {
        'mean': 6.0,
        'median': 6.0,
        'mode': 6.0
    }
    result = task_func(elements, subset_size)
    assert result == expected_result

def test_task_func_with_zero_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = 0
    with pytest.raises(ValueError):
        task_func(elements, subset_size)

def test_task_func_with_negative_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = -1
    with pytest.raises(ValueError):
        task_func(elements, subset_size)