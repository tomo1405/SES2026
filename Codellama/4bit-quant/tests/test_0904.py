import pytest
from src_0904 import task_func


def test_task_func():
    # Test case 1: Test that the function returns a LinearRegression model
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    model = task_func(d)
    assert isinstance(model, LinearRegression)

    # Test case 2: Test that the function raises a ValueError when the target variable is not in the dataframe
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    with pytest.raises(ValueError):
        task_func(d, target='w')

    # Test case 3: Test that the function raises a ValueError when the target variable is not a string
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    with pytest.raises(ValueError):
        task_func(d, target=1)

    # Test case 4: Test that the function raises a ValueError when the target variable is not in the dataframe
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    with pytest.raises(ValueError):
        task_func(d, target='w')

    # Test case 5: Test that the function returns a LinearRegression model when the target variable is a string
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    model = task_func(d, target='z')
    assert isinstance(model, LinearRegression)