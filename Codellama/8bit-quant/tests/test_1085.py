import pytest
from src_1085 import task_func
import pandas as pd
from sklearn.feature_selection import f_oneway


def test_task_func_with_one_column():
    data_file_path = "data/test_data.csv"
    df = pd.read_csv(data_file_path)
    means, std_devs, axes, anova_results = task_func(data_file_path)
    assert len(means) == 1
    assert len(std_devs) == 1
    assert len(axes) == 1
    assert anova_results is None


def test_task_func_with_multiple_columns():
    data_file_path = "data/test_data_multiple_columns.csv"
    df = pd.read_csv(data_file_path)
    means, std_devs, axes, anova_results = task_func(data_file_path)
    assert len(means) == len(df.columns)
    assert len(std_devs) == len(df.columns)
    assert len(axes) == len(df.columns)
    assert isinstance(anova_results, pd.DataFrame)
    assert anova_results.shape == (1, len(df.columns))