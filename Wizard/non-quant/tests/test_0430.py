python
import pandas as pd
import pytest
from src_0430 import task_func

def test_task_func():
    # Test case 1
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [0, 1, 0]})
    expected_selected_features = ["feature1", "feature2"]
    expected_heatmap = None
    selected_features, heatmap = task_func(df1, df2)
    assert selected_features == expected_selected_features
    assert heatmap == expected_heatmap

    # Test case 2
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [0, 1, 0]})
    expected_selected_features = ["feature1", "feature2"]
    expected_heatmap = None
    selected_features, heatmap = task_func(df1, df2)
    assert selected_features == expected_selected_features
    assert heatmap == expected_heatmap