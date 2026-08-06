import pytest
from src_0103 import task_func
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes

def test_task_func():
    fig, diabetes_df = task_func()
    
    # Check if the returned figure is an instance of plt.Figure
    assert isinstance(fig, plt.Figure), "The first return value should be an instance of matplotlib.figure.Figure"
    
    # Check if the returned dataframe is an instance of pd.DataFrame
    assert isinstance(diabetes_df, pd.DataFrame), "The second return value should be an instance of pandas.DataFrame"
    
    # Check if the dataframe has the correct number of rows and columns
    DIABETES = load_diabetes()
    expected_rows = len(DIABETES.data)
    expected_columns = len(DIABETES.feature_names)
    assert diabetes_df.shape == (expected_rows, expected_columns), f"Dataframe shape is incorrect. Expected ({expected_rows}, {expected_columns}), got {diabetes_df.shape}"
    
    # Check if the dataframe columns match the feature names
    assert all(diabetes_df.columns == DIABETES.feature_names), "DataFrame columns do not match the expected feature names"