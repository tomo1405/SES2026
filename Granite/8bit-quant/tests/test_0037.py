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
    transformed_df, fig = task_func(df)
    assert isinstance(transformed_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test if the transformed DataFrame contains the expected values
    expected_transformed_df = pd.DataFrame({
        'A': np.array([1, 2, 3, 4]),
        'B': np.array([2, 3, 4, 5]),
        'C': np.array([3, 4, 5, 6])
    })
    assert transformed_df.equals(expected_transformed_df)

    # Test if the KDE plot is generated for each column in the DataFrame
    assert len(fig.axes) == df.shape[1]