import pytest
from src_0743 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_input():
    with pytest.raises(Exception) as excinfo:
        task_func([])
    assert str(excinfo.value) == 'The input array should not be empty.'

def test_task_func_non_numeric_values():
    with pytest.raises(ValueError) as excinfo:
        task_func([['A', 'B'], ['C', 'D']])
    assert str(excinfo.value) == 'The values have to be numeric.'

def test_task_func_valid_input():
    input_data = [['A', 10], ['B', 20], ['C', 30]]
    expected_output = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'Value': [0.0, 0.5, 1.0]
    })
    
    output_df = task_func(input_data)
    
    # Check if the output DataFrame has the correct columns
    assert list(output_df.columns) == ['Category', 'Value']
    
    # Check if the 'Category' column is correct
    assert output_df['Category'].tolist() == ['A', 'B', 'C']
    
    # Check if the 'Value' column is correctly scaled
    assert all(output_df['Value'].round(2).tolist() == expected_output['Value'].tolist())

def test_task_func_single_value():
    input_data = [['A', 100]]
    expected_output = pd.DataFrame({
        'Category': ['A'],
        'Value': [0.0]
    })
    
    output_df = task_func(input_data)
    
    # Check if the output DataFrame has the correct columns
    assert list(output_df.columns) == ['Category', 'Value']
    
    # Check if the 'Category' column is correct
    assert output_df['Category'].tolist() == ['A']
    
    # Check if the 'Value' column is correctly scaled
    assert all(output_df['Value'].round(2).tolist() == expected_output['Value'].tolist())