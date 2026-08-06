import pytest
from src_0749 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_empty_selection():
    # Create a sample DataFrame
    data = {
        'Age': [25, 30, 35],
        'Weight': [60, 70, 80]
    }
    df = pd.DataFrame(data)
    
    # Test with age and weight that result in an empty selection
    result = task_func(df, 20, 100)
    assert result.empty

def test_task_func_non_empty_selection():
    # Create a sample DataFrame
    data = {
        'Age': [25, 30, 35],
        'Weight': [60, 70, 80]
    }
    df = pd.DataFrame(data)
    
    # Test with age and weight that result in a non-empty selection
    result = task_func(df, 36, 65)
    assert not result.empty

def test_task_func_standardization():
    # Create a sample DataFrame
    data = {
        'Age': [25, 30, 35],
        'Weight': [60, 70, 80]
    }
    df = pd.DataFrame(data)
    
    # Test with age and weight that result in a non-empty selection
    result = task_func(df, 36, 65)
    
    # Manually standardize the selected data to compare
    scaler = StandardScaler()
    expected_result = pd.DataFrame(scaler.fit_transform(df[['Age', 'Weight']]), columns=['Age', 'Weight'])
    
    # Check if the result is standardized correctly
    pd.testing.assert_frame_equal(result, expected_result)

def test_task_func_column_names():
    # Create a sample DataFrame
    data = {
        'Age': [25, 30, 35],
        'Weight': [60, 70, 80]
    }
    df = pd.DataFrame(data)
    
    # Test with age and weight that result in a non-empty selection
    result = task_func(df, 36, 65)
    
    # Check if the column names are preserved
    assert list(result.columns) == ['Age', 'Weight']