import pytest
from src_0711 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    temp_file = "temp.csv"
    df.to_csv(temp_file, index=False)

    # Expected result after MinMax scaling
    scaler = MinMaxScaler()
    expected_data = scaler.fit_transform(df.to_numpy())
    expected_df = pd.DataFrame(expected_data, columns=df.columns)

    # Call the function with the path to the temporary CSV file
    result_df = task_func(temp_file)

    # Check if the result matches the expected DataFrame
    assert result_df.equals(expected_df)

    # Clean up the temporary file
    import os
    os.remove(temp_file)