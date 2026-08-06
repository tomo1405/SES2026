import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0922 import task_func
import pytest

@pytest.fixture
def data():
    return [[1, 2], [3, 4], [5, 6]]

@pytest.fixture
def columns():
    return ['col1', 'col2']

def test_task_func(data, columns):
    df_copy = task_func(data, columns)
    assert isinstance(df_copy, pd.DataFrame)
    assert df_copy.shape == (3, 2)
    assert df_copy.columns.tolist() == columns

def test_task_func_with_invalid_data(data, columns):
    with pytest.raises(ValueError):
        task_func('invalid_data', columns)

def test_task_func_with_invalid_columns(data):
    with pytest.raises(ValueError):
        task_func(data, 'invalid_columns')

def test_task_func_with_invalid_data_and_columns(data):
    with pytest.raises(ValueError):
        task_func('invalid_data', 'invalid_columns')