import pytest
from src_0504 import task_func

def test_task_func():
    # Test 1: days_in_past is not an integer
    with pytest.raises(ValueError):
        task_func(days_in_past="7")

    # Test 2: days_in_past is not positive
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

    # Test 3: stock_names is not a list
    with pytest.raises(ValueError):
        task_func(stock_names="AAPL")

    # Test 4: stock_names is an empty list
    with pytest.raises(ValueError):
        task_func(stock_names=[])

    # Test 5: stock_names contains non-string elements
    with pytest.raises(ValueError):
        task_func(stock_names=[1, 2, 3])

    # Test 6: random_seed is not an integer
    with pytest.raises(ValueError):
        task_func(random_seed="0")

    # Test 7: random_seed is not positive
    with pytest.raises(ValueError):
        task_func(random_seed=-1)

    # Test 8: days_in_past is a valid integer and stock_names is a valid list of strings
    df = task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert df.columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index.dtype == np.datetime64

    # Test 9: random_seed is a valid integer and stock_names is a valid list of strings
    df = task_func(random_seed=0, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert df.columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index.dtype == np.datetime64