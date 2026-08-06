import pytest
from src_0864 import task_func

def test_task_func_with_empty_list():
    assert task_func([]) == []

def test_task_func_with_single_empty_list():
    assert task_func([[]]) == [0]

def test_task_func_with_single_list():
    assert task_func([[1]]) == [1]

def test_task_func_with_multiple_lists():
    assert task_func([[1], [2], [3]]) == [1, 5, 14]

def test_task_func_with_list_exceeding_POSSIBLE_NUMBERS_length():
    assert task_func([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [385]

def test_task_func_with_mixed_lengths():
    assert task_func([[1, 2], [3, 4, 5], [6]]) == [5, 35, 36]

def test_task_func_with_all_possible_numbers():
    assert task_func([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [385]

def test_task_func_with_zero_length_lists():
    assert task_func([[], [], []]) == [0, 0, 0]

def test_task_func_with_negative_numbers():
    with pytest.raises(ValueError):
        task_func([[-1]])

def test_task_func_with_non_integer_numbers():
    with pytest.raises(TypeError):
        task_func([[1.5]])