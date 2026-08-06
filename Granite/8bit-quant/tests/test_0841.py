import pandas as pd
import numpy as np
import pytest
from src_0841 import task_func

def test_task_func_output_type():
    file_path = 'test.csv'
    num_rows = 10
    data_dimensions = 5
    random_seed = 42
    output_file_path = task_func(file_path, num_rows, data_dimensions, random_seed)
    assert isinstance(output_file_path, str)

def test_task_func_file_content():
    file_path = 'test.csv'
    num_rows = 10
    data_dimensions = 5
    random_seed = 42
    output_file_path = task_func(file_path, num_rows, data_dimensions, random_seed)
    df = pd.read_csv(output_file_path)
    assert df.shape == (num_rows, data_dimensions)
    assert df.columns.tolist() == [f'Feature_{i + 1}' for i in range(data_dimensions)]

def test_task_func_random_seed():
    file_path = 'test.csv'
    num_rows = 10
    data_dimensions = 5
    random_seed = 42
    output_file_path_1 = task_func(file_path, num_rows, data_dimensions, random_seed)
    output_file_path_2 = task_func(file_path, num_rows, data_dimensions, random_seed)
    assert output_file_path_1 == output_file_path_2

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(123, 'abc', 5, 42)
    with pytest.raises(ValueError):
        task_func('test.csv', 10, 5, 'abc')
    with pytest.raises(ValueError):
        task_func('test.csv', 10, -1, 42)