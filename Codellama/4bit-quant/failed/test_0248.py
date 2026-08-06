import pytest
from src_0248 import task_func

def test_task_func():
    # Test that the function returns a DataFrame with the correct column names
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert result.columns.tolist() == ['Normalized Value']

    # Test that the function raises a ValueError when max_value is less than min_value
    with pytest.raises(ValueError):
        task_func(max_value=0.0, min_value=10.0)

    # Test that the function returns a DataFrame with the correct number of rows
    result = task_func(n_data_points=1000)
    assert len(result) == 1000

    # Test that the function returns a DataFrame with the correct values
    result = task_func(n_data_points=5000, min_value=0.0, max_value=10.0)
    assert result['Normalized Value'].min() >= 0.0
    assert result['Normalized Value'].max() <= 1.0