import numpy as np
import pandas as pd
from src_1140 import task_func


def test_task_func():
    # Create a sample dataset
    data = {
        'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Scores': [20, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    }
    
    # Calculate the expected MSE manually
    df = pd.DataFrame(data)
    X = df[['Hours']]
    y = df['Scores']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    expected_mse = np.mean((y_test - predictions) ** 2)
    
    # Assert that the function returns the correct MSE
    assert np.isclose(task_func(data), expected_mse)

def test_task_func_with_zero_variance():
    # Create a dataset with zero variance in the target variable
    data = {
        'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Scores': [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
    }
    
    # Calculate the expected MSE manually
    df = pd.DataFrame(data)
    X = df[['Hours']]
    y = df['Scores']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    expected_mse = np.mean((y_test - predictions) ** 2)
    
    # Assert that the function returns the correct MSE
    assert np.isclose(task_func(data), expected_mse)

def test_task_func_with_all_same_features():
    # Create a dataset where all features are the same
    data = {
        'Hours': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        'Scores': [20, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    }
    
    # Calculate the expected MSE manually
    df = pd.DataFrame(data)
    X = df[['Hours']]
    y = df['Scores']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    expected_mse = np.mean((y_test - predictions) ** 2)
    
    # Assert that the function returns the correct MSE
    assert np.isclose(task_func(data), expected_mse)