import pytest
from src_0504 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert set(result.columns) == {'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB'}, "Columns should be as specified"

    # Test with custom days_in_past
    result = task_func(days_in_past=10)
    assert len(result) == 10, "The DataFrame should have 10 rows"

    # Test with invalid days_in_past
    with pytest.raises(ValueError):
        task_func(days_in_past=-5)

    # Test with invalid stock_names
    with pytest.raises(ValueError):
        task_func(stock_names=[1, 2, 3])