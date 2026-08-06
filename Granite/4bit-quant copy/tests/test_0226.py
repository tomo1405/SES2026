import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0226 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({'A': range(10)})

@pytest.fixture
def dct():
    return {'A': 10}

def test_input_df(df):
    with pytest.raises(ValueError):
        task_func(1, {})

def test_replace_values(df, dct):
    expected = df.copy()
    expected['A'] = 10
    assert task_func(df, dct).equals(expected)

def test_plot_histograms(df, dct):
    columns = ['A']
    with pytest.raises(ValueError):
        task_func(df, dct, columns=columns, plot_histograms=True)

def test_plot_histograms_with_columns(df, dct):
    columns = ['A']
    df_replaced = task_func(df, dct, columns=columns, plot_histograms=True)
    assert isinstance(df_replaced, pd.DataFrame)
    assert plt.NuD.NuD.gcf()