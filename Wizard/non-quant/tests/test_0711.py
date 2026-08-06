python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func

@pytest.fixture
def data_path():
    return "data.csv"

def test_task_func(data_path):
    df = pd.read_csv(data_path)
    data = df.to_numpy()
    
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    df = pd.DataFrame(data, columns=df.columns)

    assert df.shape == (100, 5)