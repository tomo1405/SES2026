import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0158 import task_func


def test_task_func_input_data_not_array():
    data = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_input_data_not_2d():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_output_dataframe():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)

def test_task_func_output_ax():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data)
    assert isinstance(ax, sns.heatmap)

def test_task_func_output_dataframe_columns():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data)
    assert df.columns.tolist() == ['Average']

def test_task_func_output_dataframe_values():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data)
    assert df.values.tolist() == [[2.5], [3.5], [4.5]]