import pandas as pd
from src_0689 import task_func


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    # Standardize the dataframe
    df_standardized = task_func(df)

    # Check that the standardized dataframe has the same columns as the original dataframe
    assert df_standardized.columns.equals(df.columns)

    # Check that the standardized dataframe has the same number of rows as the original dataframe
    assert df_standardized.shape[0] == df.shape[0]

    # Check that the standardized dataframe has the same number of columns as the original dataframe
    assert df_standardized.shape[1] == df.shape[1]

    # Check that the standardized dataframe has the same values as the original dataframe, but with the mean and standard deviation subtracted
    assert df_standardized.values == df.values - scaler.mean_
    assert df_standardized.values == df.values / scaler.scale_