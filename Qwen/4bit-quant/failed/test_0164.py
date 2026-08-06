import pytest
from src_0164 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)

def test_task_func_custom_rows_and_cols():
    ax = task_func(rows=3, cols=2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)

def test_task_func_max_columns():
    ax = task_func(cols=5)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)

def test_task_func_value_error_on_too_many_columns():
    with pytest.raises(ValueError, match="Maximum number of columns allowed is 5"):
        task_func(cols=6)

def test_task_func_data_correctness():
    np.random.seed(0)
    expected_data = pd.DataFrame(np.random.rand(5, 5) * 100, columns=['A', 'B', 'C', 'D', 'E'])
    ax = task_func()
    assert ax.get_figure().get_axes()[0].get_lines()[0].get_ydata().tolist() == expected_data.iloc[0].tolist()

def test_task_func_plot_properties():
    ax = task_func()
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_figure().get_size_inches() == (10, 6)