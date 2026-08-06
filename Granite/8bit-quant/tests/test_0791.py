import pytest
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0791 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    })

def test_task_func(df):
    col1 = 'col1'
    col2 = 'col2'
    N = 3
    result = task_func(df, col1, col2, N)
    expected = [4, 3, 2]
    assert result == expected

def test_task_func_with_invalid_columns(df):
    col1 = 'col3'
    col2 = 'col4'
    N = 3
    with pytest.raises(ValueError) as excinfo:
        task_func(df, col1, col2, N)
    assert 'Columns col3 or col4 not found in the DataFrame.' in str(excinfo.value)

def test_task_func_with_invalid_N(df):
    col1 = 'col1'
    col2 = 'col2'
    N = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(df, col1, col2, N)
    assert 'N must be a positive integer.' in str(excinfo.value)

def test_task_func_with_invalid_scaler(df):
    class InvalidScaler:
        pass
    col1 = 'col1'
    col2 = 'col2'
    N = 3
    scaler = InvalidScaler()
    with pytest.raises(TypeError) as excinfo:
        task_func(df, col1, col2, N, scaler=scaler)
    assert 'scaler must be an instance of StandardScaler.' in str(excinfo.value)