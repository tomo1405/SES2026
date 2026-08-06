python
import pandas as pd
import numpy as np
import pytest

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions),
                      columns=[f'Feature_{i + 1}' for i in range(data_dimensions)])

    df.to_csv(file_path, index=False)

    return file_path

def test_task_func():
    # Test case 1: Test with default arguments
    file_path = 'test.csv'
    num_rows = 10
    data_dimensions = 5
    random_seed = None
    expected_file_path = 'test.csv'
    actual_file_path = task_func(file_path, num_rows, data_dimensions, random_seed)
    assert actual_file_path == expected_file_path

    # Test case 2: Test with custom arguments
    file_path = 'test2.csv'
    num_rows = 20
    data_dimensions = 10
    random_seed = 42
    expected_file_path = 'test2.csv'
    actual_file_path = task_func(file_path, num_rows, data_dimensions, random_seed)
    assert actual_file_path == expected_file_path