import pytest
from src_0681 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'other_feature': [7, 8, 9]
    }
    return pd.DataFrame(data)

def test_task_func_no_features(sample_df):
    result = task_func(sample_df, [])
    assert result.equals(sample_df), "The function should return the original DataFrame if no features are provided."

def test_task_func_with_features(sample_df):
    features = ['feature1', 'feature2']
    result = task_func(sample_df, features)
    
    # Check if the 'other_feature' is unchanged
    assert result['other_feature'].equals(sample_df['other_feature']), "The 'other_feature' should remain unchanged."
    
    # Check if the specified features are scaled
    scaled_values = (sample_df[features] - sample_df[features].mean()) / sample_df[features].std()
    assert result[features].equals(scaled_values), "The specified features should be scaled correctly."

def test_task_func_with_invalid_features(sample_df):
    features = ['non_existent_feature']
    with pytest.raises(KeyError):
        task_func(sample_df, features)

def test_task_func_with_all_features(sample_df):
    features = ['feature1', 'feature2', 'other_feature']
    result = task_func(sample_df, features)
    
    # Check if all features are scaled
    scaled_values = (sample_df[features] - sample_df[features].mean()) / sample_df[features].std()
    assert result[features].equals(scaled_values), "All specified features should be scaled correctly."

def test_task_func_with_single_feature(sample_df):
    features = ['feature1']
    result = task_func(sample_df, features)
    
    # Check if only the specified feature is scaled
    scaled_values = (sample_df[features] - sample_df[features].mean()) / sample_df[features].std()
    assert result[features].equals(scaled_values), "Only the specified feature should be scaled correctly."