import pytest
from src_0086 import task_func

def test_task_func():
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    random_seed = 42
    df, ax = task_func(start_date, end_date, random_seed)
    assert df.shape == (10, 4)
    assert df['Temperature'].min() >= -10 and df['Temperature'].max() <= 40
    assert df['Humidity'].min() >= 20 and df['Humidity'].max() <= 100
    assert df['Wind Speed'].min() >= 0 and df['Wind Speed'].max() <= 20
    assert ax is not None