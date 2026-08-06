import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df):
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])

    # Call the function and store the result
    result = task_func(df)

    # Define the expected result
    expected_result = pd.DataFrame([[-1.22474487, -1.22474487], [0, 0], [1.22474487, 1.22474487]], columns=['A', 'B'])

    # Use the assert statement to compare the result with the expected result
    assert result.equals(expected_result)

if __name__ == "__main__":
    pytest.main()