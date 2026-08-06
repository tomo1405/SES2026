import pytest
from src_0142 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    df, stats = task_func(5)
    assert isinstance(df, pd.DataFrame), "The result should be a DataFrame"
    assert len(df) == 5, "The DataFrame should have 5 rows"
    assert len(stats) == 6, "There should be statistics for each column"

    # Add more test cases as needed

    # Add more test cases to cover different scenarios