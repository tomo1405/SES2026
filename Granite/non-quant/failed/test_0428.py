import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pytest

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    df = pd.merge(df1, df2, on="id")
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    residuals = y - y_pred
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)  # scatter plot of residuals
    ax.axhline(y=0, color="r", linestyle="-")  # horizontal line at y=0
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot")
    return {
        "coefficients": list(model.coef_),
        "intercept": model.intercept_,
        "residuals_plot": ax,
    }

def test_task_func():
    # Test case 1: Check if the function returns the expected output for a given input
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6], "feature2": [7, 8, 9], "target": [10, 11, 12]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature1": [13, 14, 15], "feature2": [16, 17, 18], "target": [19, 20, 21]})
    expected_output = {
        "coefficients": [1.0, 1.0],
        "intercept": 0.0,
        "residuals_plot": <matplotlib.axes._subplots.AxesSubplot object at 0x7f8d2d2c0d60>,
    }
    actual_output = task_func(df1, df2)
    assert actual_output == expected_output

    # Test case 2: Check if the function raises an exception for an invalid input
    with pytest.raises(ValueError):
        task_func(df1, df2, features=["invalid_feature"], target="invalid_target")