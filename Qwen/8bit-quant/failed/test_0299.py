import pytest
from src_0299 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    return pd.DataFrame(data)

def test_task_func_no_plot(sample_df):
    result_df = task_func(sample_df, plot=False)
    assert isinstance(result_df, pd.DataFrame)
    assert 'Date' in result_df.columns
    assert all(isinstance(date, pd.Timestamp) for date in result_df['Date'])
    assert result_df.shape == (3, 3)  # Date column + 2 columns from 'Value'
    assert np.allclose(result_df.iloc[:, 1:].mean(), 0)
    assert np.allclose(result_df.iloc[:, 1:].std(), 1)

def test_task_func_with_plot(sample_df, monkeypatch):
    mock_plt = plt
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    result_df, ax = task_func(sample_df, plot=True)
    
    assert isinstance(result_df, pd.DataFrame)
    assert 'Date' in result_df.columns
    assert all(isinstance(date, pd.Timestamp) for date in result_df['Date'])
    assert result_df.shape == (3, 3)  # Date column + 2 columns from 'Value'
    assert np.allclose(result_df.iloc[:, 1:].mean(), 0)
    assert np.allclose(result_df.iloc[:, 1:].std(), 1)
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Scaled Values Over Time'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Scaled Value'

def test_task_func_invalid_column_names(sample_df):
    sample_df.columns = ['InvalidDate', 'InvalidValue']
    with pytest.raises(KeyError):
        task_func(sample_df)

def test_task_func_non_numeric_values(sample_df):
    sample_df['Value'] = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    with pytest.raises(ValueError):
        task_func(sample_df)