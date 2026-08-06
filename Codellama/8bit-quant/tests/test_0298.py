import pytest
from src_0298 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_result = {2: 2, 3: 1, 4: 1, 5: 1}
    assert task_func(elements, subset_size) == expected_result

    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    expected_result = {3: 1, 4: 1, 5: 1}
    assert task_func(elements, subset_size) == expected_result

    elements = [1, 2, 3, 4, 5]
    subset_size = 4
    expected_result = {4: 1, 5: 1}
    assert task_func(elements, subset_size) == expected_result

    elements = [1, 2, 3, 4, 5]
    subset_size = 5
    expected_result = {5: 1}
    assert task_func(elements, subset_size) == expected_result

    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    expected_result = {}
    assert task_func(elements, subset_size) == expected_result