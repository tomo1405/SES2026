python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

def test_task_func():
    data = {'Hours': [1, 2, 3, 4, 5], 'Scores': [20, 40, 60, 80, 100]}
    assert task_func(data) == 1000.0
    
    data = {'Hours': [1, 2, 3, 4, 5], 'Scores': [10, 20, 30, 40, 50]}
    assert task_func(data) == 250.0
    
    data = {'Hours': [1, 2, 3, 4, 5], 'Scores': [5, 10, 15, 20, 25]}
    assert task_func(data) == 125.0