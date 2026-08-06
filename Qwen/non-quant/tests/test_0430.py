import pytest
from src_0430 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock data for testing
@pytest.fixture
def df1():
    return pd.DataFrame({
        "id": [1, 2, 3, 4],
        "feature1": [10, 20, 30, 40],
        "feature2": [5, 15, 25, 35],
        "target": [0, 1, 0, 1]
    })

@pytest.fixture
def df2():
    return pd.DataFrame({
        "id": [1, 2, 3, 4],
        "feature3": [100, 200, 300, 400]
    })

def test_task_func(df1, df2):
    selected_features, heatmap = task_func(df1, df2)
    
    # Check if the selected features are correct
    assert isinstance(selected_features, list)
    assert len(selected_features) == 2
    assert "feature1" in selected_features
    assert "feature2" in selected_features
    
    # Check if the heatmap is a matplotlib Axes object
    assert isinstance(heatmap, plt.Axes)
    
    # Check if the merged dataframe has the correct columns
    merged_df = pd.merge(df1, df2, on="id")
    assert all(col in merged_df.columns for col in ["id", "feature1", "feature2", "feature3", "target"])
    
    # Check if the feature selection process works correctly
    features = df1.columns.drop("id")
    X = merged_df[features]
    y = merged_df["target"]
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    selected_features_from_selector = [x for x, y in zip(features, selector.get_support()) if y]
    assert selected_features == selected_features_from_selector

# Run the tests
if __name__ == "__main__":
    pytest.main()