python
import pandas as pd
import os
import pytest

from src_0631 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    filename = 'test.json'
    output_dir = './output'
    expected_file_path = os.path.join(output_dir, filename)
    file_path = task_func(df, filename, output_dir)
    assert file_path == expected_file_path
    assert os.path.exists(file_path)

    # Test case 2: Test with invalid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, None]})
    filename = 'test.json'
    output_dir = './output'
    expected_file_path = os.path.join(output_dir, filename)
    file_path = task_func(df, filename, output_dir)
    assert file_path == expected_file_path
    assert os.path.exists(file_path)

    # Test case 3: Test with non-existent output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    filename = 'test.json'
    output_dir = './non_existent_output_dir'
    expected_file_path = os.path.join(output_dir, filename)
    file_path = task_func(df, filename, output_dir)
    assert file_path == expected_file_path
    assert os.path.exists(file_path)