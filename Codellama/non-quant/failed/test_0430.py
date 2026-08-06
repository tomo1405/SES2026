import pytest
from src_0430 import task_func
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns


def test_task_func():
    # Create test dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})

    # Test that the function returns the correct output
    selected_features, heatmap = task_func(df1, df2)
    assert selected_features == ["feature1", "feature2"]
    assert isinstance(heatmap, sns.heatmap)

    # Test that the function raises an error if the input dataframes have different shapes
    df3 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300]})
    with pytest.raises(ValueError):
        task_func(df1, df3)