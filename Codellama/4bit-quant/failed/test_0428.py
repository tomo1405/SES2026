import pytest
from src_0428 import task_func

def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300], "feature3": [1000, 2000, 3000]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1000, 2000, 3000]})
    features = ["feature1", "feature2", "feature3"]
    target = "target"
    result = task_func(df1, df2, features, target)
    assert result["coefficients"] == [1, 1, 1]
    assert result["intercept"] == 0
    assert isinstance(result["residuals_plot"], matplotlib.axes.Axes)