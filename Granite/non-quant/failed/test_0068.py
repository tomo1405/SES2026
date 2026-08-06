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
    dir_path = '/path/to/directory'
    pattern = '^EMP'
    expected_df = pd.DataFrame([('EMP1.txt', 100), ('EMP2.csv', 200)], columns=['File', 'Size'])
    actual_df = task_func(dir_path, pattern)
    assert actual_df.equals(expected_df)

if __name__ == '__main__':
    pytest.main()