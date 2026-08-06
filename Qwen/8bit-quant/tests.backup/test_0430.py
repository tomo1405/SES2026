import pytest
from src_0430 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def df1():
    data = {
        "id": [1, 2, 3],
        "feature1": [10, 20, 30],
        "feature2": [15, 25, 35],
        "target": [0, 1, 0]
    }
    return pd.DataFrame(data)

@pytest.fixture
def df2():
    data = {
        "id": [1, 2, 3],
        "feature3": [12, 22, 32]
    }
    return pd.DataFrame(data)

def test_task_func_output(df1, df2):
    selected_features, heatmap = task_func(df1, df2)
    
    # Check if the selected features are correct
    assert isinstance(selected_features, list)
    assert len(selected_features) == 2
    assert set(selected_features).issubset({"feature1", "feature2"})
    
    # Check if the heatmap is a seaborn heatmap object
    assert hasattr(heatmap, 'savefig')

def test_task_func_input_validation(df1, df2):
    # Test with missing 'id' column in df1
    df1_missing_id = df1.drop(columns=['id'])
    with pytest.raises(KeyError):
        task_func(df1_missing_id, df2)
    
    # Test with missing 'id' column in df2
    df2_missing_id = df2.drop(columns=['id'])
    with pytest.raises(KeyError):
        task_func(df1, df2_missing_id)
    
    # Test with missing 'target' column in df1
    df1_missing_target = df1.drop(columns=['target'])
    with pytest.raises(KeyError):
        task_func(df1_missing_target, df2)

def test_task_func_no_features(df1, df2):
    # Modify df1 to have only 'id' and 'target' columns
    df1_no_features = df1[['id', 'target']]
    selected_features, heatmap = task_func(df1_no_features, df2)
    
    # Check if no features are selected
    assert selected_features == []
    
    # Check if the heatmap is still a seaborn heatmap object
    assert hasattr(heatmap, 'savefig')