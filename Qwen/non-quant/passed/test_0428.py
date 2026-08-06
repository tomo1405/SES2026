import pytest
from src_0428 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    df1 = pd.DataFrame({
        "id": [1, 2, 3],
        "feature1": [10, 20, 30],
        "feature2": [5, 15, 25],
        "feature3": [2, 4, 6]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3],
        "target": [100, 200, 300]
    })
    return df1, df2

def test_task_func(sample_data):
    df1, df2 = sample_data
    result = task_func(df1, df2)
    
    # Check coefficients and intercept
    assert isinstance(result["coefficients"], list)
    assert len(result["coefficients"]) == 3
    assert isinstance(result["intercept"], float)
    
    # Check residuals plot
    assert isinstance(result["residuals_plot"], plt.Axes)
    
    # Check that the plot has the correct title and labels
    assert result["residuals_plot"].get_title() == "Residuals Plot"
    assert result["residuals_plot"].get_xlabel() == "Predicted Values"
    assert result["residuals_plot"].get_ylabel() == "Residuals"
    
    # Check that the horizontal line at y=0 exists
    lines = result["residuals_plot"].lines
    assert any(line.get_ydata() == 0 for line in lines)

def test_task_func_with_custom_features(sample_data):
    df1, df2 = sample_data
    result = task_func(df1, df2, features=["feature1", "feature2"])
    
    # Check coefficients and intercept
    assert isinstance(result["coefficients"], list)
    assert len(result["coefficients"]) == 2
    assert isinstance(result["intercept"], float)
    
    # Check residuals plot
    assert isinstance(result["residuals_plot"], plt.Axes)
    
    # Check that the plot has the correct title and labels
    assert result["residuals_plot"].get_title() == "Residuals Plot"
    assert result["residuals_plot"].get_xlabel() == "Predicted Values"
    assert result["residuals_plot"].get_ylabel() == "Residuals"
    
    # Check that the horizontal line at y=0 exists
    lines = result["residuals_plot"].lines
    assert any(line.get_ydata() == 0 for line in lines)

def test_task_func_with_no_common_id():
    df1 = pd.DataFrame({
        "id": [1, 2, 3],
        "feature1": [10, 20, 30],
        "feature2": [5, 15, 25],
        "feature3": [2, 4, 6]
    })
    df2 = pd.DataFrame({
        "id": [4, 5, 6],
        "target": [100, 200, 300]
    })
    
    with pytest.raises(ValueError):
        task_func(df1, df2)