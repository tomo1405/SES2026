import pytest
from src_0107 import task_func
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def test_task_func_input_validation():
    # Test with invalid input type
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test with missing columns
    df_missing_columns = pd.DataFrame({
        'group': [1, 2],
        'date': pd.to_datetime(['2020-01-01', '2020-01-02'])
    })
    with pytest.raises(ValueError):
        task_func(df_missing_columns)

def test_task_func_data_transformation():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': pd.to_datetime(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04']),
        'value': [10, 20, 30, 40]
    })
    model, y_pred, ax = task_func(df)
    
    # Check if the date column is transformed to ordinal
    assert all(isinstance(x, int) for x in df['date'])

def test_task_func_model_prediction():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': pd.to_datetime(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04']),
        'value': [10, 20, 30, 40]
    })
    model, y_pred, ax = task_func(df)
    
    # Check if the model is an instance of LinearRegression
    assert isinstance(model, LinearRegression)
    
    # Check if predictions are of the same length as the input data
    assert len(y_pred) == len(df)

def test_task_func_plot():
    df = pd.DataFrame({
        'group': [1, 1, 2, 2],
        'date': pd.to_datetime(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04']),
        'value': [10, 20, 30, 40]
    })
    _, _, ax = task_func(df)
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Value vs Date (Linear Regression Prediction)'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'