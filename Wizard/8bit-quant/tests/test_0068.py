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
    dir_path = 'test_dir'
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, 'EMP123.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(dir_path, 'test.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(dir_path, 'EMP456.txt'), 'w') as f:
        f.write('test')

    df = task_func(dir_path)
    assert df.shape == (2, 2)
    assert df.loc[0, 'File'] == 'EMP123.txt'
    assert df.loc[0, 'Size'] == 4
    assert df.loc[1, 'File'] == 'EMP456.txt'
    assert df.loc[1, 'Size'] == 4

    os.remove(os.path.join(dir_path, 'EMP123.txt'))
    os.remove(os.path.join(dir_path, 'test.txt'))
    os.remove(os.path.join(dir_path, 'EMP456.txt'))
    os.rmdir(dir_path)