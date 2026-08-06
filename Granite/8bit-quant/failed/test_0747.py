import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from src_0747 import task_func

def test_task_func_df_should_be_a_dataframe():
    df = np.array([[1, 2], [3, 4]])
    target_column = 'target'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df should be a DataFrame." in str(excinfo.value)

def test_task_func_df_should_not_be_empty():
    df = pd.DataFrame()
    target_column = 'target'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df should contain at least one row" in str(excinfo.value)

def test_task_func_target_column_should_be_in_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_column = 'C'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "target_column should be in DataFrame" in str(excinfo.value)

def test_task_func_df_values_should_be_numeric():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [4, 5, 6]})
    target_column = 'B'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column)
    assert "df values should be numeric only" in str(excinfo.value)

def test_task_func_target_values_should_be_in_dataframe():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_column = 'A'
    target_values = [1, 3, 5]
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column, target_values)
    assert "target_values should be in DataFrame" in str(excinfo.value)

def test_task_func_target_values_should_be_numeric():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_column = 'A'
    target_values = ['a', 'b', 'c']
    with pytest.raises(ValueError) as excinfo:
        task_func(df, target_column, target_values)
    assert "target_values should be numeric only" in str(excinfo.value)

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_column = 'A'
    model = task_func(df, target_column)
    assert isinstance(model, LinearRegression)