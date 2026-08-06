import pytest
from src_0428 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    np.random.seed(0)
    df1 = pd.DataFrame({
        'id': range(1, 6),
        'feature1': np.random.rand(5),
        'feature2': np.random.rand(5),
        'feature3': np.random.rand(5)
    })
    df2 = pd.DataFrame({
        'id': range(1, 6),
        'target': np.random.rand(5)
    })
    return df1, df2

def test_task_func(sample_data):
    df1, df2 = sample_data
    result = task_func(df1, df2)
    
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "coefficients" in result, "The result should contain 'coefficients'"
    assert "intercept" in result, "The result should contain 'intercept'"
    assert "residuals_plot" in result, "The result should contain 'residuals_plot'"
    
    assert isinstance(result["coefficients"], list), "'coefficients' should be a list"
    assert isinstance(result["intercept"], (int, float)), "'intercept' should be a number"
    assert isinstance(result["residuals_plot"], plt.Axes), "'residuals_plot' should be a matplotlib Axes object"

def test_task_func_with_custom_features_and_target(sample_data):
    df1, df2 = sample_data
    df1['feature4'] = np.random.rand(5)
    df2['target2'] = np.random.rand(5)
    result = task_func(df1, df2, features=["feature1", "feature4"], target="target2")
    
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "coefficients" in result, "The result should contain 'coefficients'"
    assert "intercept" in result, "The result should contain 'intercept'"
    assert "residuals_plot" in result, "The result should contain 'residuals_plot'"
    
    assert len(result["coefficients"]) == 2, "'coefficients' should have length equal to the number of features"
    assert isinstance(result["intercept"], (int, float)), "'intercept' should be a number"
    assert isinstance(result["residuals_plot"], plt.Axes), "'residuals_plot' should be a matplotlib Axes object"