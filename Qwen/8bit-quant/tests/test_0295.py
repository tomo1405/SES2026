import pytest
from src_0295 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_basic():
    # Create a sample DataFrame
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, 35, 40],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Expected result after scaling
    scaler = StandardScaler()
    expected_age = scaler.fit_transform(df[df['id'] == 1][['age']])
    expected_income = scaler.fit_transform(df[df['id'] == 1][['income']])
    expected_df_1 = pd.DataFrame({'age': expected_age.flatten(), 'income': expected_income.flatten()}, index=[0, 1])

    scaler = StandardScaler()
    expected_age = scaler.fit_transform(df[df['id'] == 2][['age']])
    expected_income = scaler.fit_transform(df[df['id'] == 2][['income']])
    expected_df_2 = pd.DataFrame({'age': expected_age.flatten(), 'income': expected_income.flatten()}, index=[2, 3])

    expected_result = pd.concat([expected_df_1, expected_df_2]).sort_index()

    # Run the function
    result = task_func(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result, expected_result)

def test_task_func_single_group():
    # Create a sample DataFrame with a single group
    data = {
        'id': [1, 1],
        'age': [25, 30],
        'income': [50000, 60000]
    }
    df = pd.DataFrame(data)

    # Expected result after scaling
    scaler = StandardScaler()
    expected_age = scaler.fit_transform(df[['age']])
    expected_income = scaler.fit_transform(df[['income']])
    expected_df = pd.DataFrame({'age': expected_age.flatten(), 'income': expected_income.flatten()}, index=[0, 1])

    # Run the function
    result = task_func(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['id', 'age', 'income'])

    # Run the function
    result = task_func(df)

    # Check if the result is an empty DataFrame
    assert result.empty

def test_task_func_no_numeric_columns():
    # Create a DataFrame without numeric columns to scale
    data = {
        'id': [1, 1],
        'name': ['Alice', 'Bob']
    }
    df = pd.DataFrame(data)

    # Run the function and expect a ValueError
    with pytest.raises(ValueError):
        task_func(df)