import pytest
from src_0295 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, 40, 45],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Expected output after standardization
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled['age'] = scaler.fit_transform(df_scaled[['age']])
    df_scaled['income'] = scaler.fit_transform(df_scaled[['income']])
    expected_output = df_scaled.set_index('id').groupby('id').apply(lambda x: pd.DataFrame(x[['age', 'income']], index=x.index))

    # Run the function
    result = task_func(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_empty_df():
    # Test with an empty DataFrame
    df = pd.DataFrame(columns=['id', 'age', 'income'])

    # Expected output is an empty DataFrame
    expected_output = pd.DataFrame(columns=['age', 'income'])

    # Run the function
    result = task_func(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_single_row():
    # Test with a single row per group
    data = {
        'id': [1, 2],
        'age': [25, 40],
        'income': [50000, 70000]
    }
    df = pd.DataFrame(data)

    # Expected output after standardization
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled['age'] = scaler.fit_transform(df_scaled[['age']])
    df_scaled['income'] = scaler.fit_transform(df_scaled[['income']])
    expected_output = df_scaled.set_index('id').groupby('id').apply(lambda x: pd.DataFrame(x[['age', 'income']], index=x.index))

    # Run the function
    result = task_func(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_non_numeric_data():
    # Test with non-numeric data, which should raise ValueError
    data = {
        'id': [1, 1],
        'age': ['twenty-five', 'thirty'],
        'income': [50000, 60000]
    }
    df = pd.DataFrame(data)

    with pytest.raises(ValueError):
        task_func(df)