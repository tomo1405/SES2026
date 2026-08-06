import pytest
from src_0788 import task_func


def test_task_func_with_same_length_arrays():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    expected_output = 3.7416573867739413
    actual_output = task_func(array1, array2)
    assert actual_output == expected_output

def test_task_func_with_different_length_arrays():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6, 7]
    with pytest.raises(ValueError) as exc_info:
        task_func(array1, array2)
    assert "The input arrays must have the same length." in str(exc_info.value)

def test_task_func_with_empty_arrays():
    array1 = []
    array2 = []
    expected_output = 0
    actual_output = task_func(array1, array2)
    assert actual_output == expected_output