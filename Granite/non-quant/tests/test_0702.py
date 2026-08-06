import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def task_func(df, target):
    X = pd.DataFrame.drop(df, target, axis=1)  
    y = pd.Series(df[target])  
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)

def test_task_func():
    # Create a sample dataframe and target variable
    df = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6], 'y': [7, 8, 9]})
    target = 'y'

    # Call the task_func function
    score = task_func(df, target)

    # Calculate the expected score using the r2_score function
    expected_score = r2_score(df[target], df.drop(target, axis=1).dot(df.y))

    # Assert that the calculated score is equal to the expected score
    assert score == expected_score

def test_task_func_with_nan():
    # Create a sample dataframe with a missing value and target variable
    df = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, np.nan], 'y': [7, 8, 9]})
    target = 'y'

    # Call the task_func function
    score = task_func(df, target)

    # Calculate the expected score using the r2_score function
    expected_score = r2_score(df[target], df.drop(target, axis=1).dot(df.y))

    # Assert that the calculated score is equal to the expected score
    assert score == expected_score