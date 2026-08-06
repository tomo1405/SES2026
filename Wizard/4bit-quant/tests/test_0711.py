python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0711 import task_func

def test_task_func():
    # Test case 1: Test with valid data
    data_path = "data.csv"
    df = pd.read_csv(data_path)
    data = df.to_numpy()
    
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    df = pd.DataFrame(data, columns=df.columns)

    assert df.shape == (100, 5)

    # Test case 2: Test with invalid data
    data_path = "invalid_data.csv"
    with pytest.raises(FileNotFoundError):
        df = task_func(data_path)