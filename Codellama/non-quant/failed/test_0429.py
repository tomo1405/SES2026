import pytest
from src_0429 import task_func
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def test_task_func():
    # Test case 1: Both dataframes are empty
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.empty
    assert pair_plot is None

    # Test case 2: One dataframe is empty, the other is not
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.empty
    assert pair_plot is None

    # Test case 3: Both dataframes have the same columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(df1.merge(df2, on="id", how="outer"))
    assert pair_plot is None

    # Test case 4: Both dataframes have different columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [10, 20, 30], "d": [40, 50, 60]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(df1.merge(df2, on="id", how="outer"))
    assert pair_plot is None

    # Test case 5: Both dataframes have the same columns, but different values
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(df1.merge(df2, on="id", how="outer"))
    assert pair_plot is None

    # Test case 6: Both dataframes have different columns, but same values
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [10, 20, 30], "d": [40, 50, 60]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(df1.merge(df2, on="id", how="outer"))
    assert pair_plot is None

    # Test case 7: Both dataframes have different columns and different values
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [40, 50, 60]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [10, 20, 30], "d": [40, 50, 60]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(df1.merge(df2, on="id", how="outer"))
    assert pair_plot is None