import pytest
from src_0702 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Check if the score is a float and within the valid range [0, 1]
    assert isinstance(score, float), "The score should be a float."
    assert 0 <= score <= 1, "The score should be between 0 and 1."

def test_task_func_with_no_features():
    # Create a DataFrame with only the target column
    data = {
        'target': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Check if the score is 0 since there are no features to fit the model
    assert score == 0, "The score should be 0 when there are no features."

def test_task_func_with_all_zero_features():
    # Create a DataFrame with all zero features
    data = {
        'feature1': [0, 0, 0, 0, 0],
        'feature2': [0, 0, 0, 0, 0],
        'target': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Check if the score is 0 since all features are zero
    assert score == 0, "The score should be 0 when all features are zero."

def test_task_func_with_single_feature():
    # Create a DataFrame with a single feature
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Check if the score is a float and within the valid range [0, 1]
    assert isinstance(score, float), "The score should be a float."
    assert 0 <= score <= 1, "The score should be between 0 and 1."