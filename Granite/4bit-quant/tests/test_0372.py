import pytest
from src_0372 import task_func
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def test_task_func():
    # Create a sample input list
    l = [1, 2, 3, 4, 5]

    # Call the function with the sample input
    df = task_func(l)

    # Assert that the returned DataFrame has the expected shape and columns
    assert df.shape == (5, 1)
    assert df.columns.tolist() == ['Scaled Values']

    # Assert that the values in the 'Scaled Values' column are within the expected range
    scaler = MinMaxScaler()
    l_scaled = scaler.fit_transform(l.reshape(-1, 1))
    assert df['Scaled Values'].tolist() == pytest.approx(l_scaled.flatten())