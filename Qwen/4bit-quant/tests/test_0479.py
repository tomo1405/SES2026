import pytest
from src_0479 import task_func
import pandas as pd

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    seed = 42
    result_df = task_func(data_list, seed=seed)

    expected_data = {
        "Original String": ["apple, banana, cherry", "dog, elephant, frog"],
        "Modified String": ["banana, cherry", "elephant, frog"]
    }
    expected_df = pd.DataFrame(expected_data)

    assert result_df.equals(expected_df)

def test_task_func_without_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, frog"]
    result_df = task_func(data_list)

    # Since without a seed, the random choice can vary, we just check the structure
    assert "Original String" in result_df.columns
    assert "Modified String" in result_df.columns
    assert len(result_df) == len(data_list)

def test_task_func_single_element():
    data_list = ["single"]
    result_df = task_func(data_list)

    expected_data = {
        "Original String": ["single"],
        "Modified String": ["single"]
    }
    expected_df = pd.DataFrame(expected_data)

    assert result_df.equals(expected_df)

def test_task_func_empty_list():
    data_list = []
    result_df = task_func(data_list)

    expected_data = {
        "Original String": [],
        "Modified String": []
    }
    expected_df = pd.DataFrame(expected_data)

    assert result_df.equals(expected_df)