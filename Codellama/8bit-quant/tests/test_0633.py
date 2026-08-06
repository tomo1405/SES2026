import os

import pandas as pd
import pytest
from src_0633 import task_func


def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Test the function with a valid filename
    filename = 'test_output.jsonl'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert file_path.endswith('.jsonl')

    # Test the function with an invalid filename
    filename = 'test_output.csv'
    with pytest.raises(ValueError):
        task_func(df, filename)

    # Test the function with a non-existent output directory
    OUTPUT_DIR = './non_existent_dir'
    with pytest.raises(FileNotFoundError):
        task_func(df, filename)

    # Test the function with a valid output directory
    OUTPUT_DIR = './output'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert file_path.endswith('.jsonl')

    # Test the function with a large DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    for i in range(1000):
        df = pd.concat([df, df])
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert file_path.endswith('.jsonl')