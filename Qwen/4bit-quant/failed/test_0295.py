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

    # Expected result after scaling
    scaler = StandardScaler()
    expected_scaled_age = scaler.fit_transform(df[df['id'] == 1][['age']])
    expected_scaled_income = scaler.fit_transform(df[df['id'] == 1][['income']])
    expected_df = pd.DataFrame({
        'age': expected_scaled_age.flatten(),
        'income': expected_scaled_income.flatten()
    }, index=df[df['id'] == 1].index)
    
    # Call the function
    result = task_func(df)
    
    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result.loc[1], expected_df)

def test_task_func_with_invalid_data():
    # Create a sample DataFrame with invalid data
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, None, 45],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Check if the function raises a ValueError
    with pytest.raises(ValueError):
        task_func(df)