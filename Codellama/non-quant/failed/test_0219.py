import pytest
from src_0219 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler


def test_task_func_input_not_df():
    df = "not a dataframe"
    dict_mapping = {"a": "b"}
    with pytest.raises(ValueError):
        task_func(df, dict_mapping)


def test_task_func_missing_columns():
    df = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9]})
    dict_mapping = {"a": "b"}
    with pytest.raises(ValueError):
        task_func(df, dict_mapping)


def test_task_func_replace_values():
    df = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    dict_mapping = {"a": "b"}
    df_expected = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    df_actual, ax = task_func(df, dict_mapping)
    assert df_actual.equals(df_expected)


def test_task_func_standardize_features():
    df = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    dict_mapping = {"a": "b"}
    scaler = StandardScaler()
    df_expected = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    df_actual, ax = task_func(df, dict_mapping)
    assert df_actual.equals(df_expected)


def test_task_func_plot_histogram():
    df = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    dict_mapping = {"a": "b"}
    df_expected = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "feature3": [7, 8, 9], "feature4": [10, 11, 12], "feature5": [13, 14, 15], "target": [16, 17, 18]})
    df_actual, ax = task_func(df, dict_mapping, plot_histogram=True)
    assert df_actual.equals(df_expected)
    assert isinstance(ax, matplotlib.axes.Axes)