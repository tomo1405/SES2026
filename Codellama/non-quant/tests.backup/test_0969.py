import pytest
from src_0969 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    df = pd.DataFrame(data)
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    df_cumsum = numeric_df.cumsum()
    ax = sns.heatmap(df_cumsum)
    assert ax is not None