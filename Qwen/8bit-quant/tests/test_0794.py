import numpy as np
from src_0794 import task_func


def test_task_func_default_list():
    result = task_func()
    assert len(result) == 10
    assert set(result) == set(ELEMENTS)

def test_task_func_custom_list():
    custom_list = ['X', 'Y', 'Z', 'W', 'V', 'U', 'T', 'S', 'R', 'Q']
    result = task_func(custom_list)
    assert len(result) == 10
    assert set(result) == set(custom_list)

def test_task_func_random_shuffle():
    result1 = task_func()
    result2 = task_func()
    assert not np.array_equal(result1, result2), "The results should be different due to shuffling"

def test_task_func_rotation():
    result = task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    expected_first_part = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    expected_second_part = ['A', 'B', 'C']
    assert list(result[:7]) == expected_first_part
    assert list(result[7:]) == expected_second_part

def test_task_func_no_modification_of_original():
    original_list = ELEMENTS.copy()
    task_func()
    assert original_list == ELEMENTS, "The original list should not be modified"