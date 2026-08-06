import pandas as pd
import pytest
import seaborn as sns
from src_0433 import task_func


def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1, 2, 3]})
    p, heatmap = task_func(df1, df2)
    assert p > 0.05
    assert isinstance(heatmap, sns.heatmap)

def test_task_func_with_custom_column_names():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1, 2, 3]})
    p, heatmap = task_func(df1, df2, column1="feature1", column2="feature2")
    assert p > 0.05
    assert isinstance(heatmap, sns.heatmap)

def test_task_func_with_invalid_column_names():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1, 2, 3]})
    with pytest.raises(ValueError):
        p, heatmap = task_func(df1, df2, column1="invalid_column", column2="invalid_column")

def test_task_func_with_invalid_dataframe():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1, 2, 3]})
    with pytest.raises(ValueError):
        p, heatmap = task_func(df1, df2, column1="feature1", column2="feature2")