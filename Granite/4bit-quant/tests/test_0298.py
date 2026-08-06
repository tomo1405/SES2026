import pytest
from src_0298 import task_func

def test_task_func():
    elements = [1, 2, 3, 4]
    subset_size = 2
    expected_result = {3: 1, 6: 1, 7: 1, 8: 1}
    actual_result = task_func(elements, subset_size)
    assert actual_result == expected_result

def test_task_func_with_empty_list():
    elements = []
    subset_size = 0
    expected_result = {}
    actual_result = task_func(elements, subset_size)
    assert actual_result == expected_result

def test_task_func_with_invalid_subset_size():
    elements = [1, 2, 3, 4]
    subset_size = -1
    with pytest.raises(ValueError):
        task_func(elements, subset_size)