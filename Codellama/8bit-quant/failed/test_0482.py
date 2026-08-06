import pytest
from src_0482 import task_func

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, pear, grapes"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["cherry, apple, banana", "grapes, orange, pear"]})
    assert task_func(data_list) == expected_output

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "orange, pear, grapes"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["cherry, apple, banana", "grapes, orange, pear"]})
    assert task_func(data_list, seed=42) == expected_output

def test_task_func_with_different_seed():
    data_list = ["apple, banana, cherry", "orange, pear, grapes"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["cherry, apple, banana", "grapes, orange, pear"]})
    assert task_func(data_list, seed=123) != expected_output