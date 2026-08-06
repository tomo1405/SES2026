import pytest
from src_0504 import task_func

def test_task_func():
    # Test 1: days_in_past must be a positive integer
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

    # Test 2: stock_names must be a list of strings and cannot be empty
    with pytest.raises(ValueError):
        task_func(stock_names=[])

    # Test 3: stock_names must be a list of strings and cannot contain non-string elements
    with pytest.raises(ValueError):
        task_func(stock_names=[1, 2, 3])

    # Test 4: random_seed must be an integer
    with pytest.raises(ValueError):
        task_func(random_seed="abc")

    # Test 5: random_seed must be a positive integer
    with pytest.raises(ValueError):
        task_func(random_seed=-1)

    # Test 6: test the return value of the function
    df = task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert df.columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index.tolist() == pd.date_range(end=datetime.now().date(), periods=7).tolist()
    assert np.all(df.values >= 0)
    assert np.all(df.values <= 100)