import pandas as pd
from src_0127 import task_func


def test_task_func_default_animals():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert len(df) == 5
    assert all(isinstance(row['Mean'], float) for _, row in df.iterrows())
    assert all(isinstance(row['Median'], float) for _, row in df.iterrows())
    assert all(isinstance(row['Mode'], int) for _, row in df.iterrows())
    assert all(isinstance(row['Standard Deviation'], float) for _, row in df.iterrows())

def test_task_func_custom_animals():
    custom_animals = ['Dog', 'Cat', 'Mouse']
    df = task_func(custom_animals)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert len(df) == 3
    assert all(isinstance(row['Mean'], float) for _, row in df.iterrows())
    assert all(isinstance(row['Median'], float) for _, row in df.iterrows())
    assert all(isinstance(row['Mode'], int) for _, row in df.iterrows())
    assert all(isinstance(row['Standard Deviation'], float) for _, row in df.iterrows())

def test_task_func_different_seed():
    df1 = task_func(seed=123)
    df2 = task_func(seed=123)
    assert df1.equals(df2)

def test_task_func_unique_seed():
    df1 = task_func(seed=123)
    df2 = task_func(seed=456)
    assert not df1.equals(df2)

def test_task_func_mode_exists():
    df = task_func()
    for _, row in df.iterrows():
        counts = [randint(1, 100) for _ in range(10)]
        assert row['Mode'] in counts