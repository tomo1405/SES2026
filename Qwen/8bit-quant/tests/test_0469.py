import pytest
from src_0469 import task_func
import pandas as pd
import numpy as np
import os

# Mocking the file reading with a fixture
@pytest.fixture
def mock_csv_file(tmpdir):
    data = {
        'A': [1, 8, 27],
        'B': [64, 125, 216],
        'C': [343, 512, 729]
    }
    df = pd.DataFrame(data)
    csv_file = tmpdir.join("data.csv")
    df.to_csv(csv_file, index=False)
    return str(csv_file)

def test_task_func(mock_csv_file):
    df, ax, croot = task_func(file_path=mock_csv_file)
    
    # Check if the DataFrame is correctly read
    expected_df = pd.DataFrame({
        'A': [1.0, 8.0, 27.0],
        'B': [64.0, 125.0, 216.0],
        'C': [343.0, 512.0, 729.0]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the cube root calculation is correct
    expected_croot = np.cbrt(expected_df)
    np.testing.assert_array_almost_equal(croot.values, expected_croot.values)
    
    # Check if the plot axis object is created
    assert ax is not None

def test_task_func_missing_columns(mock_csv_file):
    with pytest.raises(KeyError):
        task_func(file_path=mock_csv_file, columns=["X", "Y", "Z"])

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func(file_path="nonexistent.csv")

def test_task_func_invalid_dtype(mock_csv_file):
    with pytest.raises(ValueError):
        task_func(file_path=mock_csv_file, columns=["A", "B", "C"], dtype=str)