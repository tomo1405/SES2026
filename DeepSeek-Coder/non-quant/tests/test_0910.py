import pytest
from src_0910 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert set(result.columns) == {'Letter', 'Category'}, "The DataFrame columns are incorrect"