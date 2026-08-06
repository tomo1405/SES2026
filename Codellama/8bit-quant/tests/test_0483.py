import pytest
from src_0483 import task_func

def test_task_func_remove():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 123
    expected_output = ["apple, banana", "orange, pear"]
    output = task_func(data_list, seed)
    assert output["Modified String"].tolist() == expected_output

def test_task_func_replace():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 123
    expected_output = ["random_string, banana, cherry", "orange, pear, random_string"]
    output = task_func(data_list, seed)
    assert output["Modified String"].tolist() == expected_output

def test_task_func_shuffle():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 123
    expected_output = ["cherry, banana, apple", "grape, pear, orange"]
    output = task_func(data_list, seed)
    assert output["Modified String"].tolist() == expected_output

def test_task_func_randomize():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 123
    expected_output = ["cherry, banana, apple", "grape, pear, orange"]
    output = task_func(data_list, seed)
    assert output["Modified String"].tolist() == expected_output