python
import os
import time
import pytest

from src_0630 import task_func

def test_task_func():
    # Test case 1: Test with default output directory
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
               pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})]
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 2: Test with custom output directory
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
               pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})]
    filename = 'test.csv'
    output_dir = './custom_output'
    task_func(dataset, filename, output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))

    # Test case 3: Test with empty dataset
    dataset = []
    filename = 'test.csv'
    output_dir = './output'
    task_func(dataset, filename)
    assert not os.path.exists(os.path.join(output_dir, filename))

    # Test case 4: Test with invalid output directory
    dataset = [pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
               pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})]
    filename = 'test.csv'
    output_dir = '/invalid/output/directory'
    with pytest.raises(OSError):
        task_func(dataset, filename, output_dir)