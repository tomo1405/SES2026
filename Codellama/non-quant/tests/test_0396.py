import pandas as pd
import pytest
from src_0396 import task_func


def test_task_func_valid_directory():
    directory = './'
    file_pattern = '*.txt'
    regex = r'([0-9]+)'
    df = task_func(directory, file_pattern, regex)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0

def test_task_func_invalid_directory():
    directory = './invalid_directory'
    file_pattern = '*.txt'
    regex = r'([0-9]+)'
    with pytest.raises(FileNotFoundError):
        task_func(directory, file_pattern, regex)

def test_task_func_no_files():
    directory = './'
    file_pattern = '*.invalid'
    regex = r'([0-9]+)'
    with pytest.raises(ValueError):
        task_func(directory, file_pattern, regex)

def test_task_func_invalid_regex():
    directory = './'
    file_pattern = '*.txt'
    regex = r'([0-9]+'
    with pytest.raises(ValueError):
        task_func(directory, file_pattern, regex)