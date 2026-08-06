import pytest
from src_0855 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError, match="numbers should be a list of integers."):
        task_func("not a list")

    with pytest.raises(TypeError, match="numbers should be a list of integers."):
        task_func([1, "two", 3])

def test_task_func_value_error():
    with pytest.raises(ValueError, match="each number in numbers should be non negative."):
        task_func([-1, 2, 3])

def test_task_func_empty_list():
    result = task_func([])
    assert result == ([], [])

def test_task_func_single_element():
    result = task_func([0])
    assert result == ([1], [(0,)])

def test_task_func_two_elements():
    result = task_func([1, 2])
    expected_sums = [3, 3]  # 1! + 2! = 1 + 2 = 3 and 2! + 1! = 2 + 1 = 3
    expected_permutations = [(1, 2), (2, 1)]
    assert result == (expected_sums, expected_permutations)

def test_task_func_three_elements():
    result = task_func([1, 2, 3])
    expected_sums = [9, 9, 9, 9, 9, 9]  # 1! + 2! + 3! = 1 + 2 + 6 = 9 for all permutations
    expected_permutations = [
        (1, 2, 3), (1, 3, 2),
        (2, 1, 3), (2, 3, 1),
        (3, 1, 2), (3, 2, 1)
    ]
    assert result == (expected_sums, expected_permutations)