import pytest
from src_0681 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def test_task_func_no_features():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = task_func(df, [])
    assert result.equals(df), "The DataFrame should remain unchanged if no features are provided."

def test_task_func_with_features():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    features = ['A', 'B']
    result = task_func(df, features)
    
    # Check that the features are scaled
    scaler = StandardScaler()
    expected_scaled_values = scaler.fit_transform(df[features])
    assert np.allclose(result[features].values, expected_scaled_values), "The features should be scaled correctly."
    
    # Check that the DataFrame structure is correct
    assert 'dummy' not in result.columns, "The 'dummy' column should not be present in the final DataFrame."
    assert len(result) == len(df), "The number of rows should remain unchanged."
    assert len(result.columns) == len(df.columns), "The number of columns should remain unchanged."

def test_task_func_single_feature():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    features = ['A']
    result = task_func(df, features)
    
    # Check that only the specified feature is scaled
    scaler = StandardScaler()
    expected_scaled_values = scaler.fit_transform(df[['A']])
    assert np.allclose(result['A'].values, expected_scaled_values.flatten()), "The specified feature should be scaled correctly."
    
    # Check that other features remain unchanged
    assert result['B'].equals(df['B']), "Other features should remain unchanged."
    
    # Check that the DataFrame structure is correct
    assert 'dummy' not in result.columns, "The 'dummy' column should not be present in the final DataFrame."
    assert len(result) == len(df), "The number of rows should remain unchanged."
    assert len(result.columns) == len(df.columns), "The number of columns should remain unchanged."

def test_task_func_non_numeric_features():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
    features = ['A']
    with pytest.raises(ValueError):
        task_func(df, features), "Should raise ValueError for non-numeric features."

def test_task_func_invalid_features():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    features = ['C']
    with pytest.raises(KeyError):
        task_func(df, features), "Should raise KeyError for invalid features."