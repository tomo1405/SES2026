import pytest
from src_0641 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert df.index.tolist() == MONTHS
    assert df.columns.tolist() == PRODUCTS