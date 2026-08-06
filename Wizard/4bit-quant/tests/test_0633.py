python
import os
import json
import pandas as pd
import time
import pytest

from src_0633 import task_func

OUTPUT_DIR = './output'

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Test the function with a valid filename
    filename = 'test.jsonl'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert os.path.basename(file_path) == filename

    # Test the function with an invalid filename
    filename = 'test.csv'
    with pytest.raises(ValueError):
        file_path = task_func(df, filename)

    # Test the function with a non-existent directory
    filename = 'test.jsonl'
    OUTPUT_DIR = './nonexistent_dir'
    with pytest.raises(FileNotFoundError):
        file_path = task_func(df, filename)