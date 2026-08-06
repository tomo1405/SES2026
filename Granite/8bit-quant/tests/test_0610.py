import pytest
from src_0610 import task_func

@pytest.fixture
def df():
    """
    Sample pandas DataFrame for testing.
    """
    import pandas as pd
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [16, 17, 18, 19, 20],
        'E': [21, 22, 23, 24, 25]
    })

@pytest.mark.parametrize("tuples, n_plots, expected_shape", [
    ([('A', 'B'), ('C', 'D')], 2, (5, 3)),
    ([('A', 'B'), ('C', 'D'), ('E', 'A')], 3, (5, 3)),
    ([], 5, (5, 5))
])
def test_task_func(df, tuples, n_plots, expected_shape):
    """
    Test the task_func function with different input parameters.
    """
    df, plots = task_func(df, tuples, n_plots)
    assert df.shape == expected_shape

def test_task_func_invalid_input(df):
    """
    Test the task_func function with invalid input parameters.
    """
    with pytest.raises(ValueError):
        task_func(df, 'invalid_input', -1)