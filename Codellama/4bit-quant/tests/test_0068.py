import pytest
from src_0068 import task_func

def test_task_func():
    dir_path = 'path/to/directory'
    pattern = '^EMP'
    df = task_func(dir_path, pattern)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['File', 'Size']
    assert len(df) == len(os.listdir(dir_path))
    assert all(df['File'].str.match(pattern))
    assert all(df['Size'] == df['File'].apply(lambda x: os.path.getsize(os.path.join(dir_path, x))))