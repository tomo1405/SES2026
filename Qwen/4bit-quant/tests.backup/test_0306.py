import pytest
from src_0306 import task_func

def test_task_func_with_empty_sublists():
    input_data = [[1, 2, 3], [], [4, 5]]
    result = task_func(input_data)
    assert len(result) == 8  # 5 original elements + 3 alphabets added from empty sublist

def test_task_func_no_empty_sublists():
    input_data = [[1, 2, 3], [4, 5], [6, 7]]
    result = task_func(input_data)
    assert len(result) == 7  # Only original elements

def test_task_func_with_multiple_empty_sublists():
    input_data = [[], [], []]
    result = task_func(input_data)
    assert len(result) == 30  # 10 alphabets per empty sublist

def test_task_func_with_repeated_elements():
    input_data = [[1, 1, 2, 2], [3, 3, 4, 4]]
    result = task_func(input_data)
    assert result[1] == 2 and result[2] == 2 and result[3] == 2 and result[4] == 2

def test_task_func_with_alphabet_only():
    input_data = [[], [], []]
    result = task_func(input_data)
    for key in result:
        assert key in ALPHABET

def test_task_func_with_seed():
    input_data = [[1, 2, 3], [], [4, 5]]
    result1 = task_func(input_data, seed=0)
    result2 = task_func(input_data, seed=0)
    assert result1 == result2

def test_task_func_with_different_seeds():
    input_data = [[1, 2, 3], [], [4, 5]]
    result1 = task_func(input_data, seed=0)
    result2 = task_func(input_data, seed=1)
    assert result1 != result2