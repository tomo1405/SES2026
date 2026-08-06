import pytest
from src_0103 import task_func
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes

def test_task_func():
    fig, df = task_func()
    
    # Check if the returned figure is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The first returned value should be a matplotlib Figure."
    
    # Check if the returned DataFrame is a pandas DataFrame
    assert isinstance(df, pd.DataFrame), "The second returned value should be a pandas DataFrame."
    
    # Check if the DataFrame has the correct columns
    expected_columns = load_diabetes().feature_names
    assert list(df.columns) == list(expected_columns), f"The DataFrame columns should match {expected_columns}."
    
    # Check if the DataFrame has the correct number of rows
    expected_rows = load_diabetes().data.shape[0]
    assert len(df) == expected_rows, f"The DataFrame should have {expected_rows} rows."
    
    # Check if the DataFrame has the correct number of columns
    expected_columns_count = load_diabetes().data.shape[1]
    assert len(df.columns) == expected_columns_count, f"The DataFrame should have {expected_columns_count} columns."