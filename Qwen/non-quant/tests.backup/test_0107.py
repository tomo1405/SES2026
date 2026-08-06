import pytest
from src_0107 import task_func
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Mocking the toordinal method for datetime objects
class MockDatetime:
    def toordinal(self):
        return 1

@pytest.fixture
def sample_df():
    data = {
        'group': ['A', 'A', 'B', 'B'],
        'date': [MockDatetime(), MockDatetime(), MockDatetime(), MockDatetime()],
        'value': [10, 20, 30, 40]
    }
    return pd.DataFrame(data)

def test_task_func_invalid_input_not_dataframe():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_invalid_input_missing_columns():
    df = pd.DataFrame({
        'group': ['A', 'B'],
        'date': [MockDatetime(), MockDatetime()]
    })
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input(sample_df):
    model, y_pred, ax = task_func(sample_df)
    
    assert isinstance(model, LinearRegression)
    assert isinstance(y_pred, np.ndarray)
    assert isinstance(ax, plt.Axes)
    
    # Check that the model has been fitted
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')
    
    # Check that the predictions are of the correct shape
    assert y_pred.shape == (sample_df.shape[0],)
    
    # Check that the plot is correctly configured
    assert ax.get_title() == 'Value vs Date (Linear Regression Prediction)'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'