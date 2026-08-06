import pytest
from src_0581 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The function should return a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert 'Random Numbers' in result.columns, "The DataFrame should have a column named 'Random Numbers'"
    assert 'Moving Average' in result.columns, "The DataFrame should have a column named 'Moving Average'"