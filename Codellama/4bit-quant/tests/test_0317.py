import pandas as pd
from src_0317 import task_func


def test_task_func():
    # Test that the function returns a pandas DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    df = task_func()
    assert 'Category' in df.columns
    assert 'Count' in df.columns

    # Test that the DataFrame has the correct number of rows
    assert len(df) == len(CATEGORIES)

    # Test that the values in the 'Count' column are within the specified range
    for category, count in df.itertuples(index=False):
        assert count >= 0
        assert count <= 100

    # Test that the values in the 'Category' column are the correct categories
    for category, count in df.itertuples(index=False):
        assert category in CATEGORIES