import pickle
import os
import pytest
from src_0438 import task_func

def test_task_func():
    df = {"key": [1, 2, 3]}  # Replace this with your desired input data
    file_name = "save.pkl"
    expected_output = df

    loaded_df = task_func(df, file_name)

    assert loaded_df == expected_output

def test_task_func_with_custom_file_name():
    df = {"key": [1, 2, 3]}  # Replace this with your desired input data
    file_name = "custom_save.pkl"
    expected_output = df

    loaded_df = task_func(df, file_name)

    assert loaded_df == expected_output

def test_task_func_with_invalid_file_name():
    df = {"key": [1, 2, 3]}  # Replace this with your desired input data
    file_name = 123
    with pytest.raises(TypeError):
        task_func(df, file_name)