import pytest
from src_0736 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = {'mean': 5, 'variance': 8.666666666666666}
    result = task_func(L)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_empty_list():
    L = [[]]
    expected_result = {'mean': 0, 'variance': 0}
    result = task_func(L)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_one_element_list():
    L = [[1]]
    expected_result = {'mean': 1, 'variance': 0}
    result = task_func(L)
    assert result == expected_result, "Task function returned an incorrect result"