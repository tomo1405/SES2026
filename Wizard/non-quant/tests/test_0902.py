python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler

def task_func(d):
    if not d:  # Check if the input list is empty
        return pd.DataFrame(columns=['x', 'y', 'z'])  # Return an empty DataFrame with specified columns
    
    df = pd.DataFrame(d)
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df[['x', 'y', 'z']]), columns=['x', 'y', 'z'])

    return scaled_df

# Test case 1: Valid input list
def test_task_func_valid_input():
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0, 0.5, 1], [0.5, 1, 1.5], [1, 1.5, 2]], columns=['x', 'y', 'z'])
    assert task_func(input_list).equals(expected_output)

# Test case 2: Empty input list
def test_task_func_empty_input():
    input_list = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    assert task_func(input_list).equals(expected_output)

# Test case 3: Invalid input type
def test_task_func_invalid_input():
    input_list = 'invalid input'
    with pytest.raises(TypeError):
        task_func(input_list)