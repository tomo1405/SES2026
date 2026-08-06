import pytest
from src_0396 import task_func
import os
import pandas as pd

def test_task_func_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        task_func(directory='./non_existent_dir')

def test_task_func_no_files_found():
    with pytest.raises(ValueError):
        task_func(directory='./empty_dir', file_pattern='*.txt')

def test_task_func_valid_input(tmpdir):
    # Create temporary directory and files
    dir_path = tmpdir.mkdir('test_dir')
    file1 = dir_path.join('file1.txt').write('123 abc 456')
    file2 = dir_path.join('file2.txt').write('789 def 012')

    expected_df = pd.DataFrame({
        'Filename': ['file1.txt', 'file2.txt'],
        'Numeric Data': [['123', '456'], ['789', '012']]
    })

    result_df = task_func(directory=str(dir_path), file_pattern='*.txt', regex=r'([0-9]+)')
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_custom_regex(tmpdir):
    # Create temporary directory and files
    dir_path = tmpdir.mkdir('test_dir')
    file1 = dir_path.join('file1.txt').write('abc 123 def')
    file2 = dir_path.join('file2.txt').write('ghi 456 jkl')

    expected_df = pd.DataFrame({
        'Filename': ['file1.txt', 'file2.txt'],
        'Numeric Data': [['123'], ['456']]
    })

    result_df = task_func(directory=str(dir_path), file_pattern='*.txt', regex=r'(\d+)')
    pd.testing.assert_frame_equal(result_df, expected_df)