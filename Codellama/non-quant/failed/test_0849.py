import pytest
from src_0849 import task_func

def test_task_func_empty_list():
    obj_list = []
    attr = "attr"
    top_n = 5
    seed = None

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == []
    assert random_value is None

def test_task_func_single_element_list():
    obj_list = [1]
    attr = "attr"
    top_n = 5
    seed = None

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [1]
    assert random_value == 1

def test_task_func_multiple_elements_list():
    obj_list = [1, 2, 3, 4, 5]
    attr = "attr"
    top_n = 5
    seed = None

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [5, 4, 3, 2, 1]
    assert random_value in [1, 2, 3, 4, 5]

def test_task_func_top_n_greater_than_list_length():
    obj_list = [1, 2, 3, 4, 5]
    attr = "attr"
    top_n = 10
    seed = None

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [5, 4, 3, 2, 1]
    assert random_value in [1, 2, 3, 4, 5]

def test_task_func_top_n_less_than_list_length():
    obj_list = [1, 2, 3, 4, 5]
    attr = "attr"
    top_n = 3
    seed = None

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [5, 4, 3]
    assert random_value in [1, 2, 3, 4, 5]

def test_task_func_random_seed():
    obj_list = [1, 2, 3, 4, 5]
    attr = "attr"
    top_n = 5
    seed = 1234

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [5, 4, 3, 2, 1]
    assert random_value == 1

def test_task_func_random_seed_2():
    obj_list = [1, 2, 3, 4, 5]
    attr = "attr"
    top_n = 5
    seed = 5678

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert top_values == [5, 4, 3, 2, 1]
    assert random_value == 5