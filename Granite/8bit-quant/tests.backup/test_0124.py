import pandas as pd
import os
import glob
import pytest
from src_0124 import task_func

def test_task_func_with_valid_input():
    my_list = [1, 2, 3]
    concatenated_df = task_func(my_list)
    assert isinstance(concatenated_df, pd.DataFrame)

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_with_no_files_found():
    my_list = [1, 2, 3]
    with pytest.raises(FileNotFoundError):
        task_func(my_list, file_dir='./nonexistent_directory/', file_ext='.csv')