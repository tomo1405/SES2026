import pytest
from src_1140 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Sample data
    data = {
        'Hours': [2, 3, 5, 7, 9],
        'Scores': [20, 25, 40, 48, 55]
    }
    
    # Expected result calculation
    df = pd.DataFrame(data)
    X = df[['Hours']]
    y = df['Scores']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    expected_mse = np.mean((y_test - predictions) ** 2)
    
    # Actual result
    actual_mse = task_func(data)
    
    # Asserting the results are close enough
    assert np.isclose(actual_mse, expected_mse), f"Expected MSE: {expected_mse}, but got: {actual_mse}"