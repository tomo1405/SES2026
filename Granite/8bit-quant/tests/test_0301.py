import pandas as pd
import pytest
from scipy.stats import zscore
import matplotlib.pyplot as plt
from src_0301 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Value': [10, 20, 30, 40, 50]
    })

def test_task_func(sample_df):
    df, fig = task_func(sample_df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ['Date', 'Value']
    assert df['Date'].dtype == 'datetime64[ns]'
    assert df['Value'].dtype == 'float64'
    assert fig.axes[0].get_xlabel() == 'Date'
    assert fig.axes[0].get_ylabel() == 'Z-Score'
    assert fig.axes[0].get_title() == 'Z-Scores Over Time'

def test_task_func_with_null_values(sample_df):
    sample_df.loc[2, 'Value'] = None
    df, fig = task_func(sample_df)
    assert df.shape == (5, 2)
    assert df['Value'].isnull().sum() == 1

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid input')