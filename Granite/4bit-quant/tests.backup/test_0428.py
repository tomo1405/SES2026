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
    # Mock input dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6], "target": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [10, 11, 12], "feature3": [13, 14, 15]})
    
    # Call the function
    output = task_func(df1, df2)
    
    # Assert the output is a dictionary with the expected keys
    assert isinstance(output, dict)
    assert "coefficients" in output
    assert "intercept" in output
    assert "residuals_plot" in output
    
    # Assert the coefficients and intercept have the expected shape and type
    assert isinstance(output["coefficients"], list)
    assert len(output["coefficients"]) == 3
    assert isinstance(output["intercept"], (int, float))
    
    # Assert the residuals plot is a matplotlib Axes object
    assert isinstance(output["residuals_plot"], plt.Axes)