import pytest
from src_0068 import task_func

def test_task_func():
    dir_path = 'path/to/directory'
    pattern = '^EMP'
    expected_df = pd.DataFrame({'File': ['EMP1.txt', 'EMP2.txt', 'EMP3.txt'], 'Size': [100, 200, 300]})

    df = task_func(dir_path, pattern)

    assert df.equals(expected_df)