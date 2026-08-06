import pytest
from src_0428 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300], "feature3": [1000, 2000, 3000]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1000, 2000, 3000]})
    features = ["feature1", "feature2", "feature3"]
    target = "target"
    result = task_func(df1, df2, features, target)
    assert isinstance(result, dict)
    assert "coefficients" in result
    assert "intercept" in result
    assert "residuals_plot" in result
    assert isinstance(result["coefficients"], list)
    assert isinstance(result["intercept"], float)
    assert isinstance(result["residuals_plot"], plt.Axes)