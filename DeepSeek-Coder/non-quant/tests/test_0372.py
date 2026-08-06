import pytest
from src_0372 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Normal case
    data = [1, 2, 3, 4, 5]
    expected_output = pd.DataFrame({
        'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    assert task_func(data) == expected_output

    # Add more test cases as needed