import pytest
from src_0421 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_with_numeric_columns():
    data = {
        'A': [1, 2, 3],
        'B': [4.0, 5.0, 6.0]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    
    # Check if the columns are scaled
    scaler = StandardScaler()
    expected_A = scaler.fit_transform(df[['A']]).flatten()
    expected_B = scaler.fit_transform(df[['B']]).flatten()
    
    assert all(result['A'] == expected_A), "Column 'A' is not correctly scaled"
    assert all(result['B'] == expected_B), "Column 'B' is not correctly scaled"

def test_task_func_with_mixed_columns():
    data = {
        'A': [1, 2, '3'],
        'B': ['4.0', '5.0', 'six']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    
    # Check if the columns are scaled correctly
    scaler = StandardScaler()
    converted_A = df['A'].apply(pd.to_numeric, errors='coerce')
    converted_B = df['B'].apply(pd.to_numeric, errors='coerce')
    
    expected_A = scaler.fit_transform(converted_A.dropna().values.reshape(-1, 1)).flatten()
    expected_B = scaler.fit_transform(converted_B.dropna().values.reshape(-1, 1)).flatten()
    
    assert all(result['A'][~result['A'].isna()] == expected_A), "Column 'A' is not correctly scaled"
    assert all(result['B'][~result['B'].isna()] == expected_B), "Column 'B' is not correctly scaled"

def test_task_func_with_non_numeric_columns():
    data = {
        'A': ['one', 'two', 'three'],
        'B': ['four', 'five', 'six']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    
    # Check if the columns remain unchanged
    assert all(result['A'] == df['A']), "Column 'A' should not be changed"
    assert all(result['B'] == df['B']), "Column 'B' should not be changed"

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    result = task_func(df)
    
    # Check if the empty dataframe remains empty
    assert result.empty, "Empty dataframe should remain empty"

def test_task_func_with_single_row():
    data = {
        'A': [1],
        'B': [4.0]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    
    # Check if the columns are scaled correctly
    scaler = StandardScaler()
    expected_A = scaler.fit_transform(df[['A']]).flatten()
    expected_B = scaler.fit_transform(df[['B']]).flatten()
    
    assert all(result['A'] == expected_A), "Column 'A' is not correctly scaled"
    assert all(result['B'] == expected_B), "Column 'B' is not correctly scaled"