import pytest
from src_1140 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def test_task_func():
    data = {'Hours': [10, 8, 6, 4, 2], 'Scores': [90, 80, 70, 60, 50]}
    df = pd.DataFrame(data)
    
    X = df[['Hours']]
    y = df['Scores']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    mse = np.mean((y_test - predictions) ** 2)
    
    assert mse == 0.0