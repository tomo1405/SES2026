import re
import os
import glob
import natsort
import pandas as pd
from src_0396 import task_func
def test_task_func_with_valid_directory():
    df = task_func(directory='./test_data', file_pattern='*.txt', regex=r'([0-9]+)')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ['Filename', 'Numeric Data']
    assert df.iloc[0, 0] == 'file1.txt'
    assert df.iloc[0, 1] == ['1', '2', '3']
    assert df.iloc[1, 0] == 'file2.txt'
    assert df.iloc[1, 1] == ['4', '5', '6']
def test_task_func_with_invalid_directory():
    with pytest.raises(FileNotFoundError):
        task_func(directory='invalid_directory', file_pattern='*.txt', regex=r'([0-9]+)')
def test_task_func_with_no_files_matching_pattern():
    with pytest.raises(ValueError):
        task_func(directory='./test_data', file_pattern='*.csv', regex=r'([0-9]+)')
def test_task_func_with_invalid_regex():
    with pytest.raises(re.error):
        task_func(directory='./test_data', file_pattern='*.txt', regex=r'([0-9]+')