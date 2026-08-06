import pytest
from src_0855 import task_func

def test_task_func_with_empty_list():
    result_sums, result_permutations = task_func([])
    assert result_sums == []
    assert result_permutations == []

def test_task_func_with_single_element():
    result_sums, result_permutations = task_func([0])
    assert result_sums == [1]  # factorial(0) = 1
    assert result_permutations == [(0,)]

def test_task_func_with_two_elements():
    result_sums, result_permutations = task_func([1, 2])
    expected_sums = [3, 3]  # factorial(1) + factorial(2) = 1 + 2 = 3
    expected_permutations = [(1, 2), (2, 1)]
    assert result_sums == expected_sums
    assert set(result_permutations) == set(expected_permutations)

def test_task_func_with_three_elements():
    result_sums, result_permutations = task_func([0, 1, 2])
    expected_sums = [9, 9, 9, 9, 9, 9]  # factorial(0) + factorial(1) + factorial(2) = 1 + 1 + 2 = 4
    expected_permutations = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    assert result_sums == expected_sums
    assert set(result_permutations) == set(expected_permutations)

def test_task_func_with_negative_numbers():
    with pytest.raises(ValueError):
        task_func([-1, 2])

def test_task_func_with_non_integer_elements():
    with pytest.raises(TypeError):
        task_func([1, 'a'])

def test_task_func_with_non_list_input():
    with pytest.raises(TypeError):
        task_func("not a list")