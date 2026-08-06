import pytest
from src_0303 import task_func
import pandas as pd

def test_task_func_basic():
    data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Value': [10, 20, 30]}
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert 'Value' in result.columns

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Date', 'Value'])
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_missing_columns():
    data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03']}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_plot():
    data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Value': [10, 20, 30]}
    df = pd.DataFrame(data)
    result, heatmap = task_func(df, plot=True)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(heatmap, sns.axisgrid.HeatMap)

def test_task_func_value_column_is_series():
    data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Value': [[10], [20], [30]]}
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert 'Value' in result.columns

def test_task_func_date_conversion():
    data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Value': [10, 20, 30]}
    df = pd.DataFrame(data)
    result = task_func(df)
    assert pd.api.types.is_datetime64_any_dtype(result['Date'])