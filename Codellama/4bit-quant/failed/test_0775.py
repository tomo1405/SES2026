import pytest
from src_0775 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test that the first element of the tuple is a float
    assert isinstance(result[0], float)

    # Test that the second element of the tuple is an instance of RandomForestRegressor
    assert isinstance(result[1], RandomForestRegressor)

    # Test that the function raises a ValueError when num_samples / cv is less than 2
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=2)