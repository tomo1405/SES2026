import pytest
from src_0504 import task_func

def test_task_func():
    # Test case 1: days_in_past is not an integer
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=' seven', stock_names=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'])
    assert 'days_in_past must be a positive integer.' in str(exc_info.value)

    # Test case 2: days_in_past is not positive
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=0, stock_names=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'])
    assert 'days_in_past must be a positive integer.' in str(exc_info.value)

    # Test case 3: stock_names is not a list of strings
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=7, stock_names=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 123])
    assert 'stock_names must be a list of strings and cannot be empty.' in str(exc_info.value)

    # Test case 4: stock_names is empty
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=7, stock_names=[])
    assert 'stock_names must be a list of strings and cannot be empty.' in str(exc_info.value)

    # Test case 5: Default arguments
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 5
    assert len(df) == 7