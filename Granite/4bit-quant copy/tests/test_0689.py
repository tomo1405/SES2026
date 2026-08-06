import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df):
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    # Call the function with the sample DataFrame
    result = task_func(df)

    # Define the expected result
    expected_result = pd.DataFrame({
        'A': [-1.22474487, 0.0, 1.22474487],
        'B': [-1.22474487, 0.0, 1.22474487]
    })

    # Use pytest's assert_frame_equal function to compare the result with the expected result
    assert result.equals(expected_result)