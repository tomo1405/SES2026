import pytest
from src_0430 import task_func
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

def test_task_func():
    # Create test dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})

    # Call the function with the test dataframes
    selected_features, heatmap = task_func(df1, df2)

    # Assert that the selected features are correct
    assert selected_features == ["feature1", "feature2"]

    # Assert that the heatmap is a valid Seaborn heatmap object
    assert isinstance(heatmap, sns.heatmap)