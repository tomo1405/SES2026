import pytest
from src_0483 import task_func
import pandas as pd
import random

def test_task_func_with_remove_operation():
    data_list = ["apple, banana, cherry"]
    random.seed(0)
    result_df = task_func(data_list, seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["banana, cherry"]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_replace_operation():
    data_list = ["apple, banana, cherry"]
    random.seed(1)
    result_df = task_func(data_list, seed=1)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["random_string, banana, cherry"]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_shuffle_operation():
    data_list = ["apple, banana, cherry"]
    random.seed(2)
    result_df = task_func(data_list, seed=2)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["cherry, apple, banana"]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_randomize_operation():
    data_list = ["apple, banana, cherry"]
    random.seed(3)
    result_df = task_func(data_list, seed=3)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["banana, cherry, apple"]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_single_element():
    data_list = ["apple"]
    random.seed(0)
    result_df = task_func(data_list, seed=0)
    expected_df = pd.DataFrame({
        "Original String": ["apple"],
        "Modified String": ["apple"]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_empty_list():
    data_list = []
    result_df = task_func(data_list)
    expected_df = pd.DataFrame(columns=["Original String", "Modified String"])
    assert result_df.equals(expected_df)