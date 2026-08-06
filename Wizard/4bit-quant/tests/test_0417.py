python
import pandas as pd
import seaborn as sns
import pytest

def task_func(data, column="c"):
    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    df = df.select_dtypes(include=["number"])

    if df.empty:
        return None

    return sns.heatmap(df.corr())

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = task_func(data)
    assert isinstance(result, sns.axisgrid.Grid)