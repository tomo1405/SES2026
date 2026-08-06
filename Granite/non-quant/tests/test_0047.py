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

    # Call the function and store the returned values
    df_result, axes_result = task_func(df)

    # Check if the returned values have the expected type
    assert isinstance(df_result, pd.DataFrame)
    assert isinstance(axes_result, np.ndarray)

    # Check if the returned dataframe has the expected shape
    assert df_result.shape == (5, 3)

    # Check if the missing values in the original dataframe have been filled with the column's average
    assert df_result['A'].isnull().sum() == 1
    assert df_result['B'].isnull().sum() == 1
    assert not df_result['C'].isnull().any()

    # Check if the Z-scores have been computed correctly
    assert np.array_equal(df_result['A'], zscore(df['A']))
    assert np.array_equal(df_result['B'], zscore(df['B']))
    assert np.array_equal(df_result['C'], zscore(df['C']))

    # Check if the histograms have been plotted for each numeric column
    assert len(axes_result) == 3
    assert all(isinstance(ax, plt.Axes) for ax in axes_result)

if __name__ == '__main__':
    pytest.main()