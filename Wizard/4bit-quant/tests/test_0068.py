python
import pandas as pd
import re
import os
import pytest

def task_func(dir_path: str, pattern: str = '^EMP'):
    file_sizes = []
    for file in sorted(os.listdir(dir_path)):
        if re.match(pattern, file):
            file_sizes.append((file, os.path.getsize(os.path.join(dir_path, file))))

    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    return df

def test_task_func():
    # Test case 1: Valid directory path and pattern
    dir_path = 'test_dir'
    pattern = '^EMP'
    expected_df = pd.DataFrame({'File': ['EMP1.txt', 'EMP2.txt'], 'Size': [100, 200]}, columns=['File', 'Size'])
    actual_df = task_func(dir_path, pattern)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid directory path
    dir_path = 'invalid_dir'
    pattern = '^EMP'
    with pytest.raises(FileNotFoundError):
        task_func(dir_path, pattern)

    # Test case 3: Invalid pattern
    dir_path = 'test_dir'
    pattern = 'EMP'
    with pytest.raises(re.error):
        task_func(dir_path, pattern)