import pytest
from src_0299 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_basic():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert isinstance(result_df, pd.DataFrame)
    assert 'Date' in result_df.columns
    assert result_df.shape == (3, 3)  # 3 rows and 3 columns (Date + 2 scaled values)

def test_task_func_with_plot():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    df = pd.DataFrame(data)
    result_df, ax = task_func(df, plot=True)
    assert isinstance(result_df, pd.DataFrame)
    assert 'Date' in result_df.columns
    assert result_df.shape == (3, 3)  # 3 rows and 3 columns (Date + 2 scaled values)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Date', 'Value'])
    result_df = task_func(df)
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.empty

def test_task_func_single_value():
    data = {
        'Date': ['2023-01-01'],
        'Value': [[1]]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert isinstance(result_df, pd.DataFrame)
    assert 'Date' in result_df.columns
    assert result_df.shape == (1, 2)  # 1 row and 2 columns (Date + 1 scaled value)

def test_task_func_invalid_date_format():
    data = {
        'Date': ['01/01/2023', '02/01/2023', '03/01/2023'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    df = pd.DataFrame(data)
    with pytest.raises(pd.errors.ParserError):
        task_func(df)

def test_task_func_non_numeric_values():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [['a', 'b'], [3, 4], [5, 6]]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)