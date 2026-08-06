import pytest
from src_1060 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (len(PLANETS), len(ELEMENTS)), "The DataFrame should have the correct dimensions"
    assert all(result.columns == ELEMENTS), "The columns should match the elements"