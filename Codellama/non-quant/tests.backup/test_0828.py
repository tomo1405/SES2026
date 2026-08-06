import pytest
from src_0828 import task_func

def test_task_func():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [2, 3, 5, 7]
    assert task_func(input_list) == expected_output

def test_task_func_empty_input():
    input_list = []
    expected_output = []
    assert task_func(input_list) == expected_output

def test_task_func_invalid_input():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a"]
    with pytest.raises(TypeError):
        task_func(input_list)