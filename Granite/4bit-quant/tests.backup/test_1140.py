import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
def task_func(data):
    df = pd.DataFrame(data)
    
    X = df[['Hours']]
    y = df['Scores']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    mse = np.mean((y_test - predictions) ** 2)
    
    return mse
import pytest
def test_task_func():
    data = [[1, 2], [3, 4], [5, 6]]
    expected_mse = 1.0
    actual_mse = task_func(data)
    assert actual_mse == expected_mse, "Expected MSE does not match actual MSE"
def test_task_func_with_empty_data():
    data = []
    with pytest.raises(ValueError):
        task_func(data)