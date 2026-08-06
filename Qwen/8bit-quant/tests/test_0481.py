import pytest
from src_0481 import task_func
import pandas as pd

def test_task_func_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, fox"]
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == len(data_list)
    
    # Check that the original strings are preserved
    for i, original in enumerate(data_list):
        assert result_df.loc[i, "Original String"] == original

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, fox"]
    seed = 42
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list, seed=seed)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == len(data_list)
    
    # Check that the original strings are preserved
    for i, original in enumerate(data_list):
        assert result_df.loc[i, "Original String"] == original
    
    # Check that the shuffled strings are consistent with the seed
    expected_shuffled = [
        "banana, apple, cherry",
        "elephant, dog, fox"
    ]
    for i, shuffled in enumerate(expected_shuffled):
        assert result_df.loc[i, "Shuffled String"] == shuffled

def test_task_func_empty_list():
    data_list = []
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == 0

def test_task_func_single_element():
    data_list = ["single"]
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == 1
    assert result_df.loc[0, "Original String"] == "single"
    assert result_df.loc[0, "Shuffled String"] == "single"