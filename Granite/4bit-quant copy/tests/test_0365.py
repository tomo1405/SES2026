import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'
def task_func(df):

    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
import pytest
def test_task_func():
    # Test case 1: input is a DataFrame
    df = pd.DataFrame({
        'feature 1': [1, 2, 3, 4, 5],
        'feature 2': [2, 3, 4, 5, 6],
        'feature 3': [3, 4, 5, 6, 7],
        'feature 4': [4, 5, 6, 7, 8],
        'feature 5': [5, 6, 7, 8, 9],
        'feature 6': [6, 7, 8, 9, 10],
        'feature 7': [7, 8, 9, 10, 11],
        'feature 8': [8, 9, 10, 11, 12],
        'feature 9': [9, 10, 11, 12, 13],
        'feature 10': [10, 11, 12, 13, 14],
        'target': [1, 2, 3, 4, 5]
    })
    model = task_func(df)
    assert isinstance(model, LinearRegression)

    # Test case 2: input is not a DataFrame
    with pytest.raises(ValueError):
        task_func('not a DataFrame')