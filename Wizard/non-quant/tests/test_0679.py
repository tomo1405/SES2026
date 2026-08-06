python
import pandas as pd
import json
import os
import shutil
import pytest

from src_0679 import task_func

def test_task_func():
    # Test case 1: Valid input
    path = 'data'
    expected_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'source': ['file1.json', 'file1.json', 'file1.json']})
    actual_df = task_func(path)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input (non-existent path)
    path = 'nonexistent_path'
    with pytest.raises(FileNotFoundError):
        task_func(path)

    # Test case 3: Invalid input (empty directory)
    path = 'empty_dir'
    os.makedirs(path)
    with pytest.raises(ValueError):
        task_func(path)
    shutil.rmtree(path)

    # Test case 4: Invalid input (directory with non-JSON files)
    path = 'non_json_dir'
    os.makedirs(path)
    with open(os.path.join(path, 'file1.txt'), 'w') as file:
        file.write('This is not a JSON file')
    with pytest.raises(ValueError):
        task_func(path)
    shutil.rmtree(path)

    # Test case 5: Invalid input (directory with invalid JSON files)
    path = 'invalid_json_dir'
    os.makedirs(path)
    with open(os.path.join(path, 'file1.json'), 'w') as file:
        file.write('This is not a valid JSON file')
    with pytest.raises(ValueError):
        task_func(path)
    shutil.rmtree(path)