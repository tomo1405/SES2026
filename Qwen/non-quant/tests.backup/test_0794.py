import pytest
from src_0794 import task_func
import numpy as np

def test_task_func_default():
    result = task_func()
    assert len(result) == 10
    assert set(result) == set(ELEMENTS)

def test_task_func_with_custom_list():
    custom_list = ['X', 'Y', 'Z', 'W', 'V', 'U', 'T', 'S', 'R', 'Q']
    result = task_func(custom_list)
    assert len(result) == 10
    assert set(result) == set(custom_list)

def test_task_func_preserves_elements():
    result = task_func()
    assert all(element in ELEMENTS for element in result)

def test_task_func_shuffle():
    result1 = task_func()
    result2 = task_func()
    assert not np.array_equal(result1, result2), "The function did not shuffle the list."

def test_task_func_concatenation():
    result = task_func()
    first_three = result[:3]
    remaining = result[3:]
    assert np.array_equal(np.concatenate((remaining, first_three)), result)

def test_task_func_no_modification_of_original():
    original_list = ELEMENTS.copy()
    task_func()
    assert original_list == ELEMENTS, "The original list was modified."