import pytest
from src_0299 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def test_task_func_returns_df():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)


def test_task_func_returns_ax():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    result = task_func(df, plot=True)
    assert isinstance(result, plt.Axes)


def test_task_func_scales_values():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    result = task_func(df)
    assert result.iloc[:, 1:].equals(StandardScaler().fit_transform(result.iloc[:, 1:]))


def test_task_func_plots_correctly():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    result = task_func(df, plot=True)
    assert result.get_title() == 'Scaled Values Over Time'
    assert result.get_xlabel() == 'Date'
    assert result.get_ylabel() == 'Scaled Value'