python
import pytest
from src_0761 import task_func

def test_task_func():
    df = task_func()
    assert df.shape == (100, 4)
    assert df['ID'].dtype == 'int64'
    assert df['Name'].dtype == 'object'
    assert df['Date of Birth'].dtype == 'datetime64[ns]'
    assert df['Email'].dtype == 'object'
    assert df['Email'].str.endswith('@example.com').all()
    assert df['Date of Birth'].dt.year.min() >= 1980
    assert df['Date of Birth'].dt.year.max() <= 2000