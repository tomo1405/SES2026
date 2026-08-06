import pytest
from src_0788 import task_func


def test_task_func_valid_input():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    expected_output = 5.196152422706632
    actual_output = task_func(array1, array2)
    assert actual_output == expected_output

def test_task_func_invalid_input():
    array1 = [1, 2, 3]
    array2 = [4, 5]
    with pytest.raises(ValueError):
        task_func(array1, array2)

def test_task_func_zero_length_input():
    array1 = []
    array2 = []
    expected_output = 0
    actual_output = task_func(array1, array2)
    assert actual_output == expected_output