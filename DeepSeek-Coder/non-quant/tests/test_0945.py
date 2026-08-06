import pytest
from src_0945 import task_func

def test_task_func():
    result, _ = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert 'Date' in result.columns, "The DataFrame should have a 'Date' column"
    assert 'Price' in result.columns, "The DataFrame should have a 'Price' column"