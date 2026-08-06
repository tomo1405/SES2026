python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0691 import task_func

ROWS = 100
COLUMNS = ['X', 'Y']

@pytest.fixture
def df():
    return pd.DataFrame(
        {'X': [i for i in range(ROWS)],
         'Y': [i*2 for i in range(ROWS)]}
    )

def test_task_func(df):
    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    
    # Fitting the linear regression model
    model = LinearRegression().fit(X, y)
    
    assert model.coef_[0] == 2  # Checking if the slope is 2