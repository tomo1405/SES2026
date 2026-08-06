import pytest
from src_0945 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup_test():
    np.random.seed(0)
    start_date = '2016-01-01'
    periods = 13
    freq = 'WOM-2FRI'
    seed = 0
    return start_date, periods, freq, seed

def test_task_func_output(setup_test):
    start_date, periods, freq, seed = setup_test
    prices_df, ax = task_func(start_date, periods, freq, seed)
    
    # Check DataFrame shape
    assert prices_df.shape == (periods, 1), "DataFrame shape is incorrect"
    
    # Check DataFrame index
    expected_index = pd.date_range(start=start_date, periods=periods, freq=freq)
    assert all(prices_df.index == expected_index), "DataFrame index is incorrect"
    
    # Check DataFrame values
    expected_values = np.random.uniform(low=100, high=500, size=periods)
    assert np.allclose(prices_df['Price'].values, expected_values), "DataFrame values are incorrect"
    
    # Check plot properties
    assert isinstance(ax, plt.Axes), "Return value is not a matplotlib Axes object"
    assert ax.get_title() == 'Stock Prices', "Plot title is incorrect"
    assert ax.get_xlabel() == 'Date', "Plot x-label is incorrect"
    assert ax.get_ylabel() == 'Price', "Plot y-label is incorrect"
    assert ax.gridOn, "Grid is not enabled on the plot"

def test_task_func_default_parameters():
    prices_df, ax = task_func()
    
    # Check default parameters
    assert prices_df.shape == (13, 1), "Default DataFrame shape is incorrect"
    assert prices_df.index[0] == pd.Timestamp('2016-01-01'), "Default DataFrame index is incorrect"
    assert ax.get_title() == 'Stock Prices', "Default plot title is incorrect"
    assert ax.get_xlabel() == 'Date', "Default plot x-label is incorrect"
    assert ax.get_ylabel() == 'Price', "Default plot y-label is incorrect"
    assert ax.gridOn, "Grid is not enabled on the default plot"

def test_task_func_with_different_seed():
    _, ax1 = task_func(seed=1)
    _, ax2 = task_func(seed=2)
    
    # Check that different seeds produce different plots
    assert not np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata()), "Plots with different seeds are identical"