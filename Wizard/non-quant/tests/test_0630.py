python
import os
import time
import pytest

from src_0630 import task_func

def test_task_func():
    # Test case 1: Test with a single DataFrame
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})]
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 2: Test with multiple DataFrames
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
               pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})]
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 3: Test with a non-default output directory
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})]
    filename = 'test.csv'
    output_dir = './test_output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 4: Test with an empty DataFrame
    dataset = [pd.DataFrame()]
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 5: Test with an empty list of DataFrames
    dataset = []
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 6: Test with a non-existent output directory
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})]
    filename = 'test.csv'
    output_dir = './nonexistent_output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))