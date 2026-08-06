import pytest
from src_0691 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func():
    # Create a sample DataFrame with 100 rows and columns 'X' and 'Y'
    data = {
        'X': range(ROWS),
        'Y': [2 * x + 1 for x in range(ROWS)]  # Linear relationship with some noise
    }
    df = pd.DataFrame(data)
    
    # Call the function
    model = task_func(df)
    
    # Check if the returned object is an instance of LinearRegression
    assert isinstance(model, LinearRegression), "The function should return a LinearRegression model"
    
    # Check if the model has been fitted (i.e., it has coefficients)
    assert hasattr(model, 'coef_'), "The model should have a 'coef_' attribute"
    assert hasattr(model, 'intercept_'), "The model should have an 'intercept_' attribute"
    
    # Check if the coefficients are close to the expected values (for a simple linear relationship)
    expected_coef = 2
    expected_intercept = 1
    assert abs(model.coef_[0] - expected_coef) < 1e-5, f"Expected coefficient {expected_coef}, got {model.coef_[0]}"
    assert abs(model.intercept_ - expected_intercept) < 1e-5, f"Expected intercept {expected_intercept}, got {model.intercept_}"

# Define the constant ROWS
ROWS = 100