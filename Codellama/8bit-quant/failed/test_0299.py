import pytest
from src_0299 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def test_task_func_returns_dataframe():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)


def test_task_func_returns_dataframe_with_correct_columns():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result = task_func(df)
    assert set(result.columns) == set(COLUMNS)


def test_task_func_returns_dataframe_with_correct_values():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result = task_func(df)
    assert result['Value'].tolist() == [10, 20, 30]


def test_task_func_returns_dataframe_with_correct_date_format():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result = task_func(df)
    assert result['Date'].dtype == 'datetime64[ns]'


def test_task_func_returns_dataframe_with_correct_scaled_values():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result = task_func(df)
    assert result['Value'].tolist() == [10, 20, 30]


def test_task_func_returns_dataframe_with_correct_scaled_values_when_plot_is_true():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    result, ax = task_func(df, plot=True)
    assert result['Value'].tolist() == [10, 20, 30]
    assert isinstance(ax, plt.Axes)