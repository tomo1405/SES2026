import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func
import pytest

@pytest.fixture
def data_path():
    return "path/to/data.csv"

def test_task_func_input_type(data_path):
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_output_type(data_path):
    df = task_func(data_path)
    assert isinstance(df, pd.DataFrame)

def test_task_func_output_shape(data_path):
    df = task_func(data_path)
    assert df.shape[0] > 0 and df.shape[1] > 0

def test_task_func_output_values(data_path):
    df = task_func(data_path)
    scaler = MinMaxScaler()
    data = pd.read_csv(data_path).to_numpy()
    data_scaled = scaler.fit_transform(data)
    assert df.values.tolist() == data_scaled.tolist()