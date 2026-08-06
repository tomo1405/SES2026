import pytest
from src_0034 import task_func

def test_task_func():
    list_of_pairs = [(1, 2), (3, 4), (5, 6)]
    expected_output = np.array([2 * 4 * 6])

    output = task_func(list_of_pairs)

    assert np.array_equal(output, expected_output)

def test_task_func_with_empty_list():
    list_of_pairs = []
    expected_output = np.array([1])

    output = task_func(list_of_pairs)

    assert np.array_equal(output, expected_output)

def test_task_func_with_single_pair():
    list_of_pairs = [(7, 8)]
    expected_output = np.array([8])

    output = task_func(list_of_pairs)

    assert np.array_equal(output, expected_output)