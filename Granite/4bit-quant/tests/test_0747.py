import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0747 import task_func


def test_task_func_df_should_be_a_dataframe():
    df = np.array([[1, 2], [3, 4]])
    target_column = "target"
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df should be a DataFrame." in str(excinfo.value)

def test_task_func_df_should_not_be_empty():
    df = pd.DataFrame()
    target_column = "target"
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df should contain at least one row" in str(excinfo.value)

def test_task_func_target_column_should_be_in_df_columns():
    df = pd.DataFrame()
    target_column = "target"
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "target_column should be in DataFrame" in str(excinfo.value)

def test_task_func_df_values_should_be_numeric():
    df = pd.DataFrame({"a": ["1", "2"], "b": ["3", "4"]})
    target_column = "target"
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df values should be numeric only" in str(excinfo.value)

def test_task_func_target_values_should_be_used():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    target_column = "target"
    target_values = [1, 2]
    model = task_func(df, target_column, target_values)
    assert isinstance(model, LinearRegression)