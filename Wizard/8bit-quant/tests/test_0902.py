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

def test_task_func():
    # Test case 1: Test with empty input list
    assert task_func([]) == pd.DataFrame(columns=['x', 'y', 'z'])

    # Test case 2: Test with valid input list
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0, 0.5, 1], [1, 1, 1], [1, 1, 1]], columns=['x', 'y', 'z'])
    assert task_func(input_list).equals(expected_output)

    # Test case 3: Test with invalid input list (not a list of lists)
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

    # Test case 4: Test with invalid input list (list of lists with different lengths)
    with pytest.raises(ValueError):
        task_func([[1, 2, 3], [4, 5, 6, 7], [7, 8, 9]])