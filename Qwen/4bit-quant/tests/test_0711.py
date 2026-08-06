import pytest
from src_0711 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    return pd.DataFrame(data)

@pytest.fixture
def scaled_data():
    data = {
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data, scaled_data, tmpdir):
    # Create a temporary CSV file with sample data
    temp_file = tmpdir.join("temp.csv")
    sample_data.to_csv(temp_file, index=False)

    # Call the function with the path to the temporary CSV file
    result_df = task_func(str(temp_file))

    # Check if the result matches the expected scaled data
    pd.testing.assert_frame_equal(result_df, scaled_data)

def test_task_func_with_empty_data(tmpdir):
    # Create a temporary CSV file with empty data
    temp_file = tmpdir.join("empty.csv")
    empty_df = pd.DataFrame(columns=['A', 'B'])
    empty_df.to_csv(temp_file, index=False)

    # Call the function with the path to the temporary CSV file
    result_df = task_func(str(temp_file))

    # Check if the result is an empty DataFrame with the same columns
    assert result_df.empty
    assert list(result_df.columns) == ['A', 'B']

def test_task_func_with_single_row_data(sample_data, tmpdir):
    # Create a temporary CSV file with a single row of data
    temp_file = tmpdir.join("single_row.csv")
    single_row_df = sample_data.iloc[[0]]
    single_row_df.to_csv(temp_file, index=False)

    # Call the function with the path to the temporary CSV file
    result_df = task_func(str(temp_file))

    # Check if the result is correctly scaled
    expected_scaled_data = pd.DataFrame({
        'A': [0.0],
        'B': [0.0]
    })
    pd.testing.assert_frame_equal(result_df, expected_scaled_data)

def test_task_func_with_non_numeric_data(tmpdir):
    # Create a temporary CSV file with non-numeric data
    temp_file = tmpdir.join("non_numeric.csv")
    non_numeric_data = {
        'A': [1, 'two', 3],
        'B': [4, 5, 6]
    }
    non_numeric_df = pd.DataFrame(non_numeric_data)
    non_numeric_df.to_csv(temp_file, index=False)

    # Call the function with the path to the temporary CSV file
    with pytest.raises(ValueError):
        task_func(str(temp_file))