import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0429 import task_func


@pytest.fixture
def df1():
    data = {
        "id": [1, 2, 3],
        "feature1": [10, 20, 30],
        "feature2": [100, 200, 300]
    }
    return pd.DataFrame(data)

@pytest.fixture
def df2():
    data = {
        "id": [1, 2, 4],
        "feature3": [1000, 2000, 4000]
    }
    return pd.DataFrame(data)

def test_task_func_merges_dataframes(df1, df2):
    merged_df, _ = task_func(df1, df2)
    expected_ids = sorted([1, 2, 3, 4])
    assert merged_df["id"].tolist() == expected_ids

def test_task_func_scales_numeric_features(df1, df2):
    _, _ = task_func(df1, df2)
    # Assuming the scaling is correct if the mean is close to 0 and std is close to 1
    # This is a simplified check and may need more robust testing
    assert np.isclose(df1["feature1"].mean(), 0)
    assert np.isclose(df1["feature1"].std(), 1)
    assert np.isclose(df1["feature2"].mean(), 0)
    assert np.isclose(df1["feature2"].std(), 1)

def test_task_func_returns_pair_plot(df1, df2):
    _, pair_plot = task_func(df1, df2)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)

def test_task_func_handles_empty_dataframes():
    empty_df1 = pd.DataFrame(columns=["id"])
    empty_df2 = pd.DataFrame(columns=["id"])
    merged_df, pair_plot = task_func(empty_df1, empty_df2)
    assert merged_df.empty
    assert pair_plot is None

def test_task_func_non_numeric_columns(df1, df2):
    df1["non_numeric"] = ["a", "b", "c"]
    df2["non_numeric"] = ["x", "y", "z"]
    merged_df, _ = task_func(df1, df2)
    assert "non_numeric" not in merged_df.columns

def test_task_func_no_common_columns():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30]})
    df2 = pd.DataFrame({"id2": [1, 2, 4], "feature3": [1000, 2000, 4000]})
    with pytest.raises(ValueError):
        task_func(df1, df2)