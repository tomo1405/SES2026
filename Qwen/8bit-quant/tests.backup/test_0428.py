import pytest
from src_0428 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Mock data creation
@pytest.fixture
def df1():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "feature1": [10, 20, 30],
        "feature2": [1, 2, 3],
        "feature3": [5, 10, 15]
    })

@pytest.fixture
def df2():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "target": [100, 200, 300]
    })

def test_task_func_coefficients(df1, df2):
    result = task_func(df1, df2)
    expected_coefficients = [10, 20, 30]
    assert np.allclose(result["coefficients"], expected_coefficients), "Coefficients do not match expected values"

def test_task_func_intercept(df1, df2):
    result = task_func(df1, df2)
    expected_intercept = 0
    assert np.isclose(result["intercept"], expected_intercept), "Intercept does not match expected value"

def test_task_func_residuals_plot(df1, df2):
    result = task_func(df1, df2)
    residuals_plot = result["residuals_plot"]
    assert isinstance(residuals_plot, plt.Axes), "Residuals plot is not an instance of plt.Axes"
    # Additional checks can be added to verify the plot content if needed