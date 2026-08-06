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
    df_ returned, axes_returned = task_func(df)

    # Check if the returned values are of the expected type
    assert isinstance(df_returned, pd.DataFrame)
    assert isinstance(axes_returned, np.ndarray)

    # Check if the missing values in the dataframe have been filled with the column's average
    assert df_returned['A'].isnull().sum() == 0
    assert df_returned['B'].isnull().sum() == 0

    # Check if the Z-scores have been computed correctly
    assert np.array_equal(df_returned['A'], zscore(df['A']))
    assert np.array_equal(df_returned['B'], zscore(df['B']))
    assert np.array_equal(df_returned['C'], zscore(df['C']))

    # Check if the histograms have been plotted for each numeric column
    assert len(axes_returned.flatten()) == df.shape[1]

    # Check if the layout of the histograms is as expected
    assert axes_returned.shape == (1, df.shape[1])

if __name__ == "__main__":
    pytest.main()