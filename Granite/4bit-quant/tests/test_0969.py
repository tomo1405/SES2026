import pandas as pd
import seaborn as sns
import pytest

def task_func(data):
    df = pd.DataFrame(data)
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    df_cumsum = numeric_df.cumsum()
    ax = sns.heatmap(df_cumsum)
    return ax

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = sns.heatmap(pd.DataFrame([[1, 3, 6], [10, 15, 21], [28, 44, 63]]).cumsum())
    actual_result = task_func(data)
    assert actual_result.get_figure().text[0].get_text() == expected_result.get_figure().text[0].get_text()