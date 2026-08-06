import pytest
from src_0429 import task_func
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def test_task_func_empty_df():
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.empty
    assert pair_plot is None


def test_task_func_non_empty_df():
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [1000, 2000, 3000]})
    merged_df, pair_plot = task_func(df1, df2)
    assert not merged_df.empty
    assert pair_plot is not None
    assert isinstance(pair_plot, sns.PairGrid)
    assert pair_plot.data == merged_df[["a", "b"]]


def test_task_func_scaling():
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [1000, 2000, 3000]})
    merged_df, pair_plot = task_func(df1, df2)
    assert not merged_df.empty
    assert pair_plot is not None
    assert isinstance(pair_plot, sns.PairGrid)
    assert pair_plot.data == merged_df[["a", "b"]]
    assert merged_df["a"].mean() == 0
    assert merged_df["b"].mean() == 0
    assert merged_df["a"].std() == 1
    assert merged_df["b"].std() == 1


def test_task_func_pair_plot():
    df1 = pd.DataFrame({"id": [1, 2, 3], "a": [10, 20, 30], "b": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "c": [1000, 2000, 3000]})
    merged_df, pair_plot = task_func(df1, df2)
    assert not merged_df.empty
    assert pair_plot is not None
    assert isinstance(pair_plot, sns.PairGrid)
    assert pair_plot.data == merged_df[["a", "b"]]
    assert pair_plot.axes[0, 0].get_title() == "a"
    assert pair_plot.axes[0, 1].get_title() == "b"
    assert pair_plot.axes[1, 0].get_title() == "a"
    assert pair_plot.axes[1, 1].get_title() == "b"