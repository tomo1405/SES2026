import pandas as pd
from src_0483 import task_func


def test_task_func_remove():
    data_list = ["apple, banana, cherry"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["apple, cherry"]
    })
    result = task_func(data_list, seed)
    assert result.equals(expected_output)

def test_task_func_replace():
    data_list = ["apple, banana, cherry"]
    seed = 43
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["apple, random_string, cherry"]
    })
    result = task_func(data_list, seed)
    assert result.equals(expected_output)

def test_task_func_shuffle():
    data_list = ["apple, banana, cherry"]
    seed = 44
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["banana, apple, cherry"]
    })
    result = task_func(data_list, seed)
    assert result.equals(expected_output)

def test_task_func_randomize():
    data_list = ["apple, banana, cherry"]
    seed = 45
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["cherry, apple, banana"]
    })
    result = task_func(data_list, seed)
    assert result.equals(expected_output)

def test_task_func_single_element():
    data_list = ["apple"]
    seed = 46
    expected_output = pd.DataFrame({
        "Original String": ["apple"],
        "Modified String": ["apple"]
    })
    result = task_func(data_list, seed)
    assert result.equals(expected_output)

def test_task_func_empty_list():
    data_list = []
    seed = 47
    expected_output = pd.DataFrame(columns=["Original String", "Modified String"])
    result = task_func(data_list, seed)
    assert result.equals(expected_output)