import pandas as pd
from src_0429 import task_func


def test_task_func():
    # Test case 1: Both dataframes are empty
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.empty
    assert pair_plot is None

    # Test case 2: Both dataframes have the same columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "C": [10, 11, 12], "D": [13, 14, 15]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9], "C": [10, 11, 12], "D": [13, 14, 15]}))
    assert pair_plot is None

    # Test case 3: Both dataframes have different columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "C": [10, 11, 12], "D": [13, 14, 15]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9], "C": [10, 11, 12], "D": [13, 14, 15]}))
    assert pair_plot is None

    # Test case 4: One dataframe is empty
    df1 = pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9]})
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9]}))
    assert pair_plot is None

    # Test case 5: Both dataframes have numeric columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "C": [10, 11, 12], "D": [13, 14, 15]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(pd.DataFrame({"id": [1, 2, 3], "A": [4, 5, 6], "B": [7, 8, 9], "C": [10, 11, 12], "D": [13, 14, 15]}))
    assert pair_plot is not None

    # Test case 6: Both dataframes have non-numeric columns
    df1 = pd.DataFrame({"id": [1, 2, 3], "A": ["a", "b", "c"], "B": ["d", "e", "f"]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "C": ["g", "h", "i"], "D": ["j", "k", "l"]})
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.equals(pd.DataFrame({"id": [1, 2, 3], "A": ["a", "b", "c"], "B": ["d", "e", "f"], "C": ["g", "h", "i"], "D": ["j", "k", "l"]}))
    assert pair_plot is None