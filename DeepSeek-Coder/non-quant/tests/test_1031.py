import pytest
from src_1031 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (17576, 3), "The DataFrame should have the correct shape"
    assert list(result.columns) == ["Letter 1", "Letter 2", "Letter 3"], "The columns should be named correctly"