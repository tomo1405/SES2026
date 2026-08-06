import pytest
from src_0037 import task_func

def test_task_func():
    import pandas as pd
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt

    # Create a sample DataFrame with some negative values
    df = pd.DataFrame({
        'A': np.array([1, 2, -1, 4]),
        'B': np.array([2, 3, 4, 5]),
        'C': np.array([3, 4, 5, 6])
    })

    # Test if the function raises a ValueError when the DataFrame contains negative values
    with pytest.raises(ValueError):
        task_func(df)

    # Create a new DataFrame with only positive values
    df = pd.DataFrame({
        'A': np.array([1, 2, 3, 4]),
        'B': np.array([2, 3, 4, 5]),
        'C': np.array([3, 4, 5, 6])
    })

    # Test if the function returns a tuple with two elements
    result = task_func(df)
    assert len(result) == 2

    # Test if the first element of the tuple is a DataFrame
    assert isinstance(result[0], pd.DataFrame)

    # Test if the second element of the tuple is a Figure
    assert isinstance(result[1], plt.Figure)