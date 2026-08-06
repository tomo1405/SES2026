import pytest
from src_0248 import task_func

def test_task_func():
    # Test case 1: Test that the function raises a ValueError when max_value is less than min_value
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=0.0)

    # Test case 2: Test that the function returns a DataFrame with the correct number of rows
    data = task_func(n_data_points=5000, min_value=0.0, max_value=10.0)
    assert len(data) == 5000

    # Test case 3: Test that the function returns a DataFrame with the correct column names
    assert data.columns.tolist() == ['Normalized Value']

    # Test case 4: Test that the function returns a DataFrame with the correct data types
    assert data.dtypes.tolist() == ['float64']

    # Test case 5: Test that the function returns a DataFrame with the correct values
    expected_data = [round(random.uniform(0.0, 10.0), 3) for _ in range(5000)]
    assert data.values.tolist() == expected_data