import pytest
from src_1030 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (100, 3), "The DataFrame should have 100 rows and 3 columns"
    assert all(result.columns == ['a', 'b', 'c']), "The columns should be named 'a', 'b', 'c'"