import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from src_0299 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })

def test_task_func(input_df):
    output_df = task_func(input_df)
    assert isinstance(output_df, pd.DataFrame)
    assert list(output_df.columns) == ['Date', 'Value']
    assert output_df['Date'].dtype == 'datetime64[ns]'
    assert output_df['Value'].dtype == 'float64'

def test_task_func_plot(input_df):
    output_df, ax = task_func(input_df, plot=True)
    assert isinstance(ax, plt.Axes)
    assert isinstance(output_df, pd.DataFrame)
    assert list(output_df.columns) == ['Date', 'Value']
    assert output_df['Date'].dtype == 'datetime64[ns]'
    assert output_df['Value'].dtype == 'float64'