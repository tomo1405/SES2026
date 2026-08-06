import pytest
from src_0641 import task_func

def test_task_func():
    result = task_func()
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert len(result.index) == len(MONTHS)
    assert len(result.columns) == len(PRODUCTS)