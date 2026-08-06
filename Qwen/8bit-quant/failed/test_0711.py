import pytest
from src_0711 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Mocking the pandas read_csv function to simulate file reading
def mock_read_csv(path):
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    return pd.DataFrame(data)

# Patching the pandas module to use the mock function
@pytest.fixture(autouse=True)
def patch_pandas(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func():
    # Define the path (not used in mock, but required by the function signature)
    data_path = "dummy_path.csv"
    
    # Expected result after scaling
    expected_data = {
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0]
    }
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(data_path)
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_empty_data():
    # Mocking an empty DataFrame
    def mock_empty_read_csv(path):
        return pd.DataFrame(columns=['A', 'B'])
    
    # Patching the pandas module to use the mock function
    @pytest.fixture(autouse=True)
    def patch_pandas_empty(monkeypatch):
        monkeypatch.setattr(pd, 'read_csv', mock_empty_read_csv)
    
    # Define the path (not used in mock, but required by the function signature)
    data_path = "empty_dummy_path.csv"
    
    # Expected result is an empty DataFrame with the same columns
    expected_df = pd.DataFrame(columns=['A', 'B'])
    
    # Call the function
    result_df = task_func(data_path)
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)