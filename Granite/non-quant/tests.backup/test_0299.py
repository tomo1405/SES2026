import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from unittest.mock import patch

from src_0299 import task_func

def test_task_func_with_plot():
    df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })
    with patch('matplotlib.pyplot.show') as mock_show:
        df_result, ax_result = task_func(df, plot=True)
        mock_show.assert_called_once()
    assert isinstance(df_result, pd.DataFrame)
    assert isinstance(ax_result, plt.Axes)
    assert df_result.shape == (3, 2)
    assert df_result.columns.tolist() == ['Date', 'Value']
    assert df_result['Date'].dtype == 'datetime64[ns]'
    assert df_result['Value'].dtype == 'float64'
    assert ax_result.get_title() == 'Scaled Values Over Time'
    assert ax_result.get_xlabel() == 'Date'
    assert ax_result.get_ylabel() == 'Scaled Value'

def test_task_func_without_plot():
    df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })
    df_result = task_func(df, plot=False)
    assert isinstance(df_result, pd.DataFrame)
    assert df_result.shape == (3, 2)
    assert df_result.columns.tolist() == ['Date', 'Value']
    assert df_result['Date'].dtype == 'datetime64[ns]'
    assert df_result['Value'].dtype == 'float64'