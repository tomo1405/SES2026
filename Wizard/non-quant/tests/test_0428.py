python
import pandas as pd
import pytest
from src_0428 import task_func

def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6], "target": [7, 8, 9]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature3": [7, 8, 9], "target": [10, 11, 12]})
    result = task_func(df1, df2)
    assert isinstance(result, dict)
    assert "coefficients" in result
    assert "intercept" in result
    assert "residuals_plot" in result
    assert isinstance(result["coefficients"], list)
    assert isinstance(result["intercept"], float)
    assert isinstance(result["residuals_plot"], plt.Axes)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func("df1", "df2")