import pytest
from src_0052 import task_func
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Mocking the plt.show to prevent actual plotting during tests
plt.show = lambda: None

@pytest.fixture
def sample_df():
    data = {
        "Age": [25, 30, 35, 40, 45, 50],
        "Height": [160, 170, 180, 190, 200, 210]
    }
    return pd.DataFrame(data)

def test_task_func_no_clusters(sample_df):
    age_threshold = 45
    height_threshold = 180
    result_df, ax = task_func(sample_df, age_threshold, height_threshold)
    assert result_df.equals(sample_df)
    assert ax is None
    assert result_df["Cluster"].unique() == [0]

def test_task_func_with_clusters(sample_df):
    age_threshold = 20
    height_threshold = 220
    result_df, ax = task_func(sample_df, age_threshold, height_threshold)
    assert len(result_df) >= 3
    assert "Cluster" in result_df.columns
    assert result_df["Cluster"].nunique() == 3
    assert ax is not None

def test_task_func_edge_case(sample_df):
    age_threshold = 40
    height_threshold = 200
    result_df, ax = task_func(sample_df, age_threshold, height_threshold)
    assert len(result_df) == 2
    assert "Cluster" in result_df.columns
    assert result_df["Cluster"].unique() == [0]
    assert ax is None

def test_task_func_empty_input():
    empty_df = pd.DataFrame(columns=["Age", "Height"])
    age_threshold = 30
    height_threshold = 180
    result_df, ax = task_func(empty_df, age_threshold, height_threshold)
    assert result_df.empty
    assert ax is None