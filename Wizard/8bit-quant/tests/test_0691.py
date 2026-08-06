python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    
    # Fitting the linear regression model
    model = LinearRegression().fit(X, y)
    
    return model

def test_task_func():
    # Creating a sample dataframe
    df = pd.DataFrame(columns=COLUMNS, data=np.random.rand(ROWS, len(COLUMNS)))
    
    # Testing the function
    model = task_func(df)
    assert isinstance(model, LinearRegression)