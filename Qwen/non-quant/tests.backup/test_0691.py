import pytest
from src_0691 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_with_valid_data():
    # Create a sample DataFrame with 100 rows and columns 'X' and 'Y'
    data = {'X': range(ROWS), 'Y': [2 * x + 1 for x in range(ROWS)]}
    df = pd.DataFrame(data)
    
    # Call the task_func
    model = task_func(df)
    
    # Check if the returned object is an instance of LinearRegression
    assert isinstance(model, LinearRegression)
    
    # Check if the model has been fitted (i.e., it has coefficients)
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['X', 'Y'])
    
    # Call the task_func
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    
    # Check if the error message indicates that the input data is empty
    assert "Input data must contain at least one row" in str(excinfo.value)

def test_task_func_with_missing_columns():
    # Create a DataFrame with missing columns 'X' or 'Y'
    df = pd.DataFrame({'X': range(ROWS)})
    
    # Call the task_func
    with pytest.raises(KeyError) as excinfo:
        task_func(df)
    
    # Check if the error message indicates that the required columns are missing
    assert "Column 'Y' is missing" in str(excinfo.value)

    df = pd.DataFrame({'Y': range(ROWS)})
    
    # Call the task_func
    with pytest.raises(KeyError) as excinfo:
        task_func(df)
    
    # Check if the error message indicates that the required columns are missing
    assert "Column 'X' is missing" in str(excinfo.value)