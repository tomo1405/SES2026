import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func
import pytest

@pytest.fixture
def data_path():
    return "path/to/data.csv"

def test_task_func(data_path):
    df = task_func(data_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0

def test_task_func_with_invalid_data_path(data_path):
    with pytest.raises(FileNotFoundError):
        task_func("invalid/path")

def test_task_func_with_invalid_data(data_path):
    invalid_data_path = "path/to/invalid_data.csv"
    with open(invalid_data_path, "w") as f:
        f.write("invalid data")
    with pytest.raises(ValueError):
        task_func(invalid_data_path)