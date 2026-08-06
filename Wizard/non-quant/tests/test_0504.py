python
import pytest
from src_0504 import task_func

def test_task_func():
    # Test valid inputs
    df = task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert df.index.dtype == "datetime64[ns]"
    assert df.columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.values.max() <= 100
    assert df.values.min() >= 0
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        task_func(days_in_past=-1, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0)
    with pytest.raises(ValueError):
        task_func(days_in_past=7, stock_names=[], random_seed=0)
    with pytest.raises(ValueError):
        task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", 123], random_seed=0)