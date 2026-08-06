import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func
import pytest

def test_task_func():
    data_path = "path/to/data.csv"
    df = pd.read_csv(data_path)
    data = df.to_numpy()

    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    df = pd.DataFrame(data, columns=df.columns)

    assert task_func(data_path).equals(df)

def test_task_func_with_invalid_data_path():
    data_path = "invalid/path/to/data.csv"
    with pytest.raises(FileNotFoundError):
        task_func(data_path)

def test_task_func_with_invalid_data():
    data_path = "path/to/invalid_data.csv"
    df = pd.DataFrame({"A": [1, 2, "three"]})
    with pytest.raises(ValueError):
        task_func(data_path)