import pytest
from src_0681 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_features():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(df, [])
    assert result.equals(df)

def test_task_func_with_features():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
    features = ['A', 'B']
    result = task_func(df, features)
    
    # Check that the features are scaled
    scaler = StandardScaler()
    expected_scaled = scaler.fit_transform(df[features])
    assert np.allclose(result.loc[:, features].values, expected_scaled)
    
    # Check that other columns remain unchanged
    assert result['C'].equals(df['C'])

def test_task_func_all_features():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    features = ['A', 'B']
    result = task_func(df, features)
    
    # Check that all features are scaled
    scaler = StandardScaler()
    expected_scaled = scaler.fit_transform(df[features])
    assert np.allclose(result.values, expected_scaled)

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['A', 'B'])
    features = ['A', 'B']
    result = task_func(df, features)
    assert result.equals(df)

def test_task_func_single_feature():
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    features = ['A']
    result = task_func(df, features)
    
    # Check that the feature is scaled
    scaler = StandardScaler()
    expected_scaled = scaler.fit_transform(df[features])
    assert np.allclose(result.values, expected_scaled)