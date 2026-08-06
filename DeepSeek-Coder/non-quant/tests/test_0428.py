import pytest
from src_0428 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Mock data for testing
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "feature1": [1, 2, 3],
    "feature2": [4, 5, 6],
    "feature3": [7, 8, 9],
    "target": [10, 11, 12]
})

df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "feature1": [1, 2, 3],
    "feature2": [4, 5, 6],
    "feature3": [7, 8, 9],
    "target": [10, 11, 12]
})

def test_task_func():
    result = task_func(df1, df2)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert "coefficients" in result, "The result should contain coefficients."
    assert "intercept" in result, "The result should contain the intercept."
    assert "residuals_plot" in result, "The result should contain the residuals plot."
    assert isinstance(result["coefficients"], list), "The coefficients should be a list."
    assert isinstance(result["intercept"], (int, float)), "The intercept should be a number."
    assert isinstance(result["residuals_plot"], plt.Axes), "The residuals plot should be a matplotlib Axes object."

pytest.main()