import pytest
from src_0194 import task_func

def test_task_func():
    result = task_func(5, 3)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result.columns) == 3, "The DataFrame should have the correct number of columns"
    assert len(result) == 5, "The DataFrame should have the correct number of rows"
    assert all(result.dtypes[col] in [int, float] for col in result.columns), "The DataFrame should contain the correct data types"