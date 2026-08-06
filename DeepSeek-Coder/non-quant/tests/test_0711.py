import pytest
from src_0711 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    df_path = 'test_data.csv'
    df.to_csv(df_path, index=False)

    # Call the function with the test data
    result = task_func(df_path)

    # Assertions to verify the output
    assert result.shape == (5, 2)
    assert result.iloc[0, 0] == 0.0  # First feature should be scaled between 0 and 1
    assert result.iloc[0, 1] == 1.0  # Second feature should be scaled between 0 and 1

    # Clean up the test data
    import os
    os.remove(df_path)