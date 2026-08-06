import pytest
from src_0047 import task_func

def test_task_func():
    import pandas as pd
    import numpy as np
    from scipy.stats import zscore
    import matplotlib.pyplot as plt

    # Create a sample dataframe with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, 5]
    })

    # Call the function
    df_transformed, axes = task_func(df)

    # Check if the returned values are of the expected type
    assert isinstance(df_transformed, pd.DataFrame)
    assert isinstance(axes, np.ndarray)

    # Check if the dataframe has been modified in place
    assert df_transformed is not df

    # Check if the missing values have been filled with the column's average
    assert df_transformed['A'].isna().sum() == 1
    assert df_transformed['B'].isna().sum() == 1
    assert np.isclose(df_transformed['A'].mean(), 3)
    assert np.isclose(df_transformed['B'].mean(), 3)

    # Check if the Z-scores have been computed correctly
    assert np.allclose(df_transformed['A'], zscore(df['A']))
    assert np.allclose(df_transformed['B'], zscore(df['B']))
    assert np.allclose(df_transformed['C'], zscore(df['C']))

    # Check if the histograms have been plotted
    assert len(axes.flatten()) == df.shape[1]
    assert all(isinstance(ax, plt.Axes) for ax in axes.flatten())