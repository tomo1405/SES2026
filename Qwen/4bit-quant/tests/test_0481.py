import pytest
from src_0481 import task_func
import pandas as pd

def test_task_func_with_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (2, 2)
    assert all(result_df.columns == ["Original String", "Shuffled String"])
    assert result_df.iloc[0]["Original String"] == "apple, banana, cherry"
    assert result_df.iloc[1]["Original String"] == "dog, elephant, frog"

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    seed = 42
    result_df = task_func(data_list, seed=seed)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (2, 2)
    assert all(result_df.columns == ["Original String", "Shuffled String"])
    assert result_df.iloc[0]["Original String"] == "apple, banana, cherry"
    assert result_df.iloc[1]["Original String"] == "dog, elephant, frog"
    assert result_df.iloc[0]["Shuffled String"] == "banana, apple, cherry"
    assert result_df.iloc[1]["Shuffled String"] == "elephant, dog, frog"

def test_task_func_empty_list():
    data_list = []
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (0, 2)
    assert all(result_df.columns == ["Original String", "Shuffled String"])

def test_task_func_single_element():
    data_list = ["apple"]
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (1, 2)
    assert all(result_df.columns == ["Original String", "Shuffled String"])
    assert result_df.iloc[0]["Original String"] == "apple"
    assert result_df.iloc[0]["Shuffled String"] == "apple"

def test_task_func_multiple_commas():
    data_list = ["apple,, banana,, cherry"]
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (1, 2)
    assert all(result_df.columns == ["Original String", "Shuffled String"])
    assert result_df.iloc[0]["Original String"] == "apple,, banana,, cherry"
    # The shuffled string should have the same number of elements and order
    assert result_df.iloc[0]["Shuffled String"] == "apple,, banana,, cherry"