import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0064 import task_func

@pytest.fixture
def car_dict():
    return {'Car1': 'Red', 'Car2': 'Blue', 'Car3': 'Red', 'Car4': 'Green', 'Car5': 'Blue'}

def test_task_func(car_dict):
    df, ax = task_func(car_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_columns(car_dict):
    df, ax = task_func(car_dict)
    assert df.columns.tolist() == ['Car', 'Color']

def test_task_func_data(car_dict):
    df, ax = task_func(car_dict)
    assert df.loc[0, 'Car'] == 'Car1'
    assert df.loc[0, 'Color'] == 'Red'
    assert df.loc[4, 'Car'] == 'Car5'
    assert df.loc[4, 'Color'] == 'Blue'

def test_task_func_plot(car_dict):
    df, ax = task_func(car_dict)
    assert ax.get_xlabel() == 'Color'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Distribution of Vehicle Colors'