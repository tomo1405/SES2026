import pytest
from src_0689 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df)

    # Check if the result is a DataFrame
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"

    # Check if the number of columns is the same
    assert result.shape[1] == df.shape[1], "The number of columns should be the same"

    # Check if the values are standardized
    mean = result.mean()
    std = result.std()
    assert abs(mean) < 1e-6, "The values should be standardized"
    assert abs(std - 1) < 1e-6, "The values should be standardized"