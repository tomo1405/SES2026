python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Valid input DataFrame
    df = pd.DataFrame({'A': [1, 3, 4], 'B': [2, 4, 6]})
    transformed_df, fig = task_func(df)
    assert transformed_df.shape == (3, 2)
    assert isinstance(fig, plt.Figure)

    # Test case 2: Invalid input DataFrame (contains negative values)
    df = pd.DataFrame({'A': [1, 3, -4], 'B': [2, 4, 6]})
    try:
        transformed_df, fig = task_func(df)
    except ValueError as e:
        assert str(e) == "Input DataFrame should contain only positive values."

    # Test case 3: Input DataFrame with constant values
    df = pd.DataFrame({'A': [1, 1, 1], 'B': [2, 2, 2]})
    transformed_df, fig = task_func(df)
    assert transformed_df.shape == (3, 2)
    assert isinstance(fig, plt.Figure)

    # Test case 4: Input DataFrame with null values
    df = pd.DataFrame({'A': [1, 3, np.nan], 'B': [2, 4, 6]})
    transformed_df, fig = task_func(df)
    assert transformed_df.shape == (3, 2)
    assert isinstance(fig, plt.Figure)