import pytest
from src_0317 import task_func

def test_task_func():
    # Test that the function returns a pandas DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert list(task_func().columns) == ['Category', 'Count']

    # Test that the DataFrame has the correct number of rows
    assert len(task_func()) == len(CATEGORIES)

    # Test that the values in the 'Count' column are within the specified range
    assert all(task_func()['Count'] >= 0)
    assert all(task_func()['Count'] <= 100)

    # Test that the values in the 'Category' column are from the CATEGORIES list
    assert all(task_func()['Category'].isin(CATEGORIES))