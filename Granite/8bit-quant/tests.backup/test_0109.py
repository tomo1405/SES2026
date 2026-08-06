import pandas as pd
import pytest
from src_0109 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'group': ['A', 'B', 'A', 'B'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'value': [10, 20, 30, 40]
    })

def test_task_func_valid_input(df):
    result, ax = task_func(df)
    assert isinstance(result, seasonal_decompose)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_df(df):
    df_invalid = df.drop('group', axis=1)
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns."):
        task_func(df_invalid)

def test_task_func_invalid_decomposition_model(df):
    with pytest.raises(ValueError, match="Invalid 'decomposition_model': must be 'additive' or 'multiplicative'."):
        task_func(df, decomposition_model='invalid')

def test_task_func_invalid_freq(df):
    with pytest.raises(ValueError, match="Invalid 'freq': must be a string representing frequency."):
        task_func(df, freq=123)

def test_task_func_missing_value(df):
    df_missing = df.copy()
    df_missing.loc[0, 'value'] = None
    with pytest.raises(ValueError, match="Non-numeric or missing values found in 'value' column."):
        task_func(df_missing)