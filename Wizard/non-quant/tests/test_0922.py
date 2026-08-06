python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    df = pd.DataFrame(data)
    # Create a local MinMaxScaler object
    scaler = MinMaxScaler()
    
    # Create a copy of the DataFrame to avoid modifying the original DataFrame
    df_copy = df.copy()

    # Normalize the specified columns
    df_copy[columns] = scaler.fit_transform(df_copy[columns])

    return df_copy

def test_task_func():
    # Test case 1: Test with valid input data
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 2: Test with invalid input data (non-numeric values)
    data = {'A': [1, 2, 3], 'B': ['4', '5', '6']}
    columns = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(data, columns)

    # Test case 3: Test with invalid input data (empty columns list)
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = []
    with pytest.raises(ValueError):
        task_func(data, columns)

    # Test case 4: Test with invalid input data (non-existent column)
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A', 'C']
    with pytest.raises(KeyError):
        task_func(data, columns)