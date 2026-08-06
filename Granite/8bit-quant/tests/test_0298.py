import pytest
from src_0298 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    expected_result = {15: 1, 14: 1, 13: 1, 12: 1, 11: 1}
    result = task_func(elements, subset_size)
    assert result == expected_result

def test_task_func_with_empty_elements():
    elements = []
    subset_size = 3
    expected_result = {}
    result = task_func(elements, subset_size)
    assert result == expected_result

def test_task_func_with_negative_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = -1
    with pytest.raises(ValueError):
        task_func(elements, subset_size)