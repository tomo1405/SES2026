import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df, target):
    X = pd.DataFrame.drop(df, target, axis=1)  
    y = pd.Series(df[target])  
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)

def test_task_func():
    # Test case 1: Check if the function raises an error if the input dataframe is empty
    df = pd.DataFrame()
    target = 'target'
    with pytest.raises(ValueError):
        task_func(df, target)

    # Test case 2: Check if the function returns a score between 0 and 1
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    target = 'y'
    score = task_func(df, target)
    assert 0 <= score <= 1

    # Test case 3: Check if the function returns the same score for the same input dataframe
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4]})
    target = 'y'
    score1 = task_func(df, target)
    score2 = task_func(df, target)
    assert score1 == score2