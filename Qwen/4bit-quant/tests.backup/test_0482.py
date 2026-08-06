import pytest
from src_0482 import task_func

def test_task_func():
    # Test with a simple list of strings
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    expected_columns = ["Original String", "Randomized String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert all(col in result_df.columns for col in expected_columns)
    assert len(result_df) == len(data_list)
    
    # Check that the original strings are preserved
    assert result_df.iloc[0]["Original String"] == "apple, banana, cherry"
    assert result_df.iloc[1]["Original String"] == "dog, elephant, frog"
    
    # Check that the randomized strings are correctly shuffled
    original_substrings_0 = set("apple, banana, cherry".split(", "))
    original_substrings_1 = set("dog, elephant, frog".split(", "))
    
    randomized_substrings_0 = set(result_df.iloc[0]["Randomized String"].split(", "))
    randomized_substrings_1 = set(result_df.iloc[1]["Randomized String"].split(", "))
    
    assert original_substrings_0 == randomized_substrings_0
    assert original_substrings_1 == randomized_substrings_1

def test_task_func_with_empty_list():
    # Test with an empty list
    data_list = []
    expected_columns = ["Original String", "Randomized String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert all(col in result_df.columns for col in expected_columns)
    assert result_df.empty

def test_task_func_with_single_string():
    # Test with a single string
    data_list = ["cat, mouse"]
    expected_columns = ["Original String", "Randomized String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert all(col in result_df.columns for col in expected_columns)
    assert len(result_df) == 1
    
    # Check that the original and randomized strings are the same
    assert result_df.iloc[0]["Original String"] == "cat, mouse"
    assert result_df.iloc[0]["Randomized String"] == "cat, mouse"

def test_task_func_with_same_substrings():
    # Test with a string having the same substring multiple times
    data_list = ["bird, bird, bird"]
    expected_columns = ["Original String", "Randomized String"]
    
    result_df = task_func(data_list)
    
    assert isinstance(result_df, pd.DataFrame)
    assert all(col in result_df.columns for col in expected_columns)
    assert len(result_df) == 1
    
    # Check that the original and randomized strings are the same
    assert result_df.iloc[0]["Original String"] == "bird, bird, bird"
    assert result_df.iloc[0]["Randomized String"] == "bird, bird, bird"