import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from src_1026 import task_func
import pytest

@pytest.fixture
def data_dict():
    return {'A': [1, 2, 3], 'B': [4, 5, 6]}

def test_task_func(data_dict):
    df_scaled, ax = task_func(data_dict)
    assert isinstance(df_scaled, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df_scaled.shape == (3, 2)
    assert ax.get_title() == "Scaled Values"

def test_task_func_with_empty_data(data_dict):
    data_dict['A'] = [None, None, None]
    df_scaled, ax = task_func(data_dict)
    assert df_scaled.empty
    assert ax.get_title() == "Scaled Values"