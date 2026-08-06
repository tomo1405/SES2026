import pytest
from src_0702 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 5, 7, 11]
    }
    df = pd.DataFrame(data)
    
    # Define the target column
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Assert that the score is a float between 0 and 1
    assert isinstance(score, float)
    assert 0 <= score <= 1

def test_task_func_with_no_features():
    # Create a DataFrame with only the target column
    data = {
        'target': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    
    # Define the target column
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Assert that the score is 0 since there are no features
    assert score == 0

def test_task_func_with_constant_target():
    # Create a DataFrame with constant target values
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    
    # Define the target column
    target = 'target'
    
    # Call the function
    score = task_func(df, target)
    
    # Assert that the score is 0 since the target is constant
    assert score == 0