import pandas as pd
import re
import os
import pytest
from src_0068 import task_func

def test_task_func():
    dir_path = '/path/to/directory'
    pattern = '^EMP'
    file_sizes = []
    for file in sorted(os.listdir(dir_path)):
        if re.match(pattern, file):
            file_sizes.append((file, os.path.getsize(os.path.join(dir_path, file))))

    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    expected_df = task_func(dir_path, pattern)
    assert expected_df.equals(df)

def test_task_func_with_invalid_pattern():
    dir_path = '/path/to/directory'
    pattern = '^invalid_pattern'
    with pytest.raises(ValueError):
        task_func(dir_path, pattern)

def test_task_func_with_invalid_dir_path():
    dir_path = '/path/to/invalid_directory'
    pattern = '^EMP'
    with pytest.raises(FileNotFoundError):
        task_func(dir_path, pattern)