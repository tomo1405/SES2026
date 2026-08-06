import pytest
from src_0125 import task_func

def test_task_func_with_valid_input():
    my_list = [1, 2, 3, 4, 5]
    size = 100
    seed = 100
    expected_output = (float, type(plt.gca()))
    actual_output = task_func(my_list, size, seed)
    assert isinstance(actual_output[0], expected_output[0])
    assert isinstance(actual_output[1], expected_output[1])

def test_task_func_with_invalid_input():
    my_list = "not a list"
    size = 100
    seed = 100
    with pytest.raises(TypeError):
        task_func(my_list, size, seed)

def test_task_func_with_invalid_list_elements():
    my_list = [1, 2, "not a number", 4, 5]
    size = 100
    seed = 100
    with pytest.raises(ValueError):
        task_func(my_list, size, seed)