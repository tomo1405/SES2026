import re

import pandas as pd
from src_0481 import task_func


def test_task_func_with_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == len(data_list)
    
    for original, shuffled in zip(result_df["Original String"], result_df["Shuffled String"]):
        original_substrings = set(re.split(r"\s*,\s*", original))
        shuffled_substrings = set(re.split(r"\s*,\s*", shuffled))
        assert original_substrings == shuffled_substrings

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    seed = 42
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list, seed=seed)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == len(data_list)
    
    for original, shuffled in zip(result_df["Original String"], result_df["Shuffled String"]):
        original_substrings = set(re.split(r"\s*,\s*", original))
        shuffled_substrings = set(re.split(r"\s*,\s*", shuffled))
        assert original_substrings == shuffled_substrings
    
    # Check that the shuffling is reproducible with the same seed
    result_df_repeat = task_func(data_list, seed=seed)
    assert result_df.equals(result_df_repeat)

def test_task_func_empty_list():
    data_list = []
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert result_df.empty

def test_task_func_single_element():
    data_list = ["single"]
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == 1
    assert result_df.iloc[0]["Original String"] == "single"
    assert result_df.iloc[0]["Shuffled String"] == "single"

def test_task_func_single_word_elements():
    data_list = ["apple", "banana", "cherry"]
    expected_columns = ["Original String", "Shuffled String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == expected_columns
    assert len(result_df) == len(data_list)
    
    for original, shuffled in zip(result_df["Original String"], result_df["Shuffled String"]):
        assert original == shuffled