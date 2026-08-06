import pandas as pd
import pytest
from src_0517 import task_func


def test_task_func():
    # Test that the function returns a tuple of a DataFrame and a RegressionResultsWrapper
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, results = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

    # Test that the function raises a ValueError if the input array is not a 2D list
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test that the function raises a ValueError if the input array is not a list of lists
    with pytest.raises(ValueError):
        task_func("hello")

    # Test that the function raises a ValueError if the input array is not a list of lists with 5 elements
    with pytest.raises(ValueError):
        task_func([[1, 2, 3, 4, 5, 6]])

    # Test that the function raises a ValueError if the input array is not a list of lists with 5 elements
    with pytest.raises(ValueError):
        task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])