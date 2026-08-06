import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from unittest.mock import patch

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
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "feature2": [7, 8, 9]})
    expected_result = {
        "coefficients": [1.0, 1.0],
        "intercept": 0.0,
        "residuals_plot": None,
    }
    with patch("matplotlib.pyplot.show") as mock_show:
        result = task_func(df1, df2)
    mock_show.assert_called_once()
    assert result == expected_result

def test_task_func_with_custom_features():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6], "feature2": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "feature3": [10, 11, 12]})
    expected_result = {
        "coefficients": [1.0, 1.0],
        "intercept": 0.0,
        "residuals_plot": None,
    }
    with patch("matplotlib.pyplot.show") as mock_show:
        result = task_func(df1, df2, features=["feature1", "feature3"])
    mock_show.assert_called_once()
    assert result == expected_result

def test_task_func_with_custom_target():
    df1 = pd.DataFrame({"id": [1, 2, 3], "target": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "target": [7, 8, 9]})
    expected_result = {
        "coefficients": [1.0, 1.0],
        "intercept": 0.0,
        "residuals_plot": None,
    }
    with patch("matplotlib.pyplot.show") as mock_show:
        result = task_func(df1, df2, target="target")
    mock_show.assert_called_once()
    assert result == expected_result