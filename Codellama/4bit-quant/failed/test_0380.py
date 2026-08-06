import pytest
from src_0380 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(10), pd.DataFrame)

    # Test that the DataFrame has the correct number of rows and columns
    assert task_func(10).shape == (10, 5)

    # Test that the DataFrame has the correct column names
    assert task_func(10).columns.tolist() == COLUMNS

    # Test that the DataFrame contains only integers
    assert np.all(task_func(10).astype(int) == task_func(10))