import pytest
from src_0303 import task_func
import pandas as pd

def test_task_func_basic():
    data = {
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({'Value': [1.0]}))

def test_task_func_with_plot():
    data = {
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    result, heatmap = task_func(df, plot=True)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({'Value': [1.0]}))
    assert isinstance(heatmap, sns.axisgrid.FacetGrid)

def test_task_func_empty_df():
    df = pd.DataFrame(columns=['Date', 'Value'])
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_missing_columns():
    data = {
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_invalid_date_format():
    data = {
        'Date': ['not-a-date', '2020-01-02', '2020-01-03'],
        'Value': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    with pytest.raises(pd.errors.ParserError):
        task_func(df)