import pytest
from src_0483 import task_func
import pandas as pd

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant", "fish"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry", "dog, elephant", "fish"],
        "Modified String": ["banana, cherry", "elephant", "fish"]
    })
    
    result_df = task_func(data_list, seed=seed)
    assert result_df.equals(expected_output)

def test_task_func_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant", "fish"]
    result_df = task_func(data_list)
    assert "Original String" in result_df.columns
    assert "Modified String" in result_df.columns
    assert len(result_df) == len(data_list)

def test_task_func_single_element():
    data_list = ["single_element"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["single_element"],
        "Modified String": ["single_element"]
    })
    
    result_df = task_func(data_list, seed=seed)
    assert result_df.equals(expected_output)

def test_task_func_empty_list():
    data_list = []
    expected_output = pd.DataFrame(columns=["Original String", "Modified String"])
    
    result_df = task_func(data_list)
    assert result_df.equals(expected_output)

def test_task_func_replace_operation():
    data_list = ["apple, banana, cherry"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["random_string, banana, cherry"]
    })
    
    result_df = task_func(data_list, seed=seed)
    assert result_df.equals(expected_output)

def test_task_func_shuffle_operation():
    data_list = ["apple, banana, cherry"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["banana, apple, cherry"]
    })
    
    result_df = task_func(data_list, seed=seed)
    assert result_df.equals(expected_output)

def test_task_func_randomize_operation():
    data_list = ["apple, banana, cherry"]
    seed = 42
    expected_output = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Modified String": ["cherry, banana, apple"]
    })
    
    result_df = task_func(data_list, seed=seed)
    assert result_df.equals(expected_output)