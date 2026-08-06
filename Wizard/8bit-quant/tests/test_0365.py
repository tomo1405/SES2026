python
import pandas as pd
import pytest
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

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'feature 1': [1, 2, 3, 4, 5], 'feature 2': [6, 7, 8, 9, 10], 'target': [11, 12, 13, 14, 15]})
    model = task_func(df)
    assert isinstance(model, LinearRegression)

    # Test case 2: Invalid input
    with pytest.raises(ValueError):
        task_func(123)