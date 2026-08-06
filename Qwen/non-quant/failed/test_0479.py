import pytest
from src_0479 import task_func

def test_task_func_with_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog", "grape, honeydew, kiwi"]
    df = task_func(data_list)
    
    assert "Original String" in df.columns
    assert "Modified String" in df.columns
    assert len(df) == 3
    
    # Check that the original strings are correct
    for i, s in enumerate(data_list):
        assert df.at[i, "Original String"] == s.strip()
    
    # Check that the modified strings are different from the original strings
    for i, s in enumerate(data_list):
        assert df.at[i, "Modified String"] != s.strip()

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog", "grape, honeydew, kiwi"]
    seed = 42
    df1 = task_func(data_list, seed=seed)
    df2 = task_func(data_list, seed=seed)
    
    assert df1.equals(df2), "DataFrames should be equal with the same seed"

def test_task_func_with_single_element():
    data_list = ["apple"]
    df = task_func(data_list)
    
    assert len(df) == 1
    assert df.at[0, "Original String"] == "apple"
    assert df.at[0, "Modified String"] == "apple"

def test_task_func_with_empty_string():
    data_list = [""]
    df = task_func(data_list)
    
    assert len(df) == 1
    assert df.at[0, "Original String"] == ""
    assert df.at[0, "Modified String"] == ""

def test_task_func_with_whitespace():
    data_list = ["   "]
    df = task_func(data_list)
    
    assert len(df) == 1
    assert df.at[0, "Original String"] == "   "
    assert df.at[0, "Modified String"] == "   "

def test_task_func_with_single_substring():
    data_list = ["apple, banana"]
    df = task_func(data_list)
    
    assert len(df) == 1
    assert df.at[0, "Original String"] == "apple, banana"
    assert df.at[0, "Modified String"] != "apple, banana"