python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6], "target": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature3": [7, 8, 9], "target": [10, 11, 12]})
    result = task_func(df1, df2)
    assert result["coefficients"] == [0.0, 0.0, 1.0]
    assert result["intercept"] == 0.0
    assert isinstance(result["residuals_plot"], plt.Axes)