import pytest
from src_0532 import task_func
import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt

# Mocking KMeans to avoid actual computation and plotting
class MockKMeans:
    def __init__(self, n_clusters, random_state, n_init):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.n_init = n_init

    def fit_predict(self, X):
        return [0] * len(X)

@pytest.fixture
def mock_kmeans(monkeypatch):
    monkeypatch.setattr(KMeans, "__init__", MockKMeans.__init__)
    monkeypatch.setattr(KMeans, "fit_predict", MockKMeans.fit_predict)

def test_task_func_with_no_duplicates(mock_kmeans):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df)
    
    assert duplicates_counter == Counter()
    assert len(unique_df) == 3
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].tolist() == [0, 0, 0]

def test_task_func_with_duplicates(mock_kmeans):
    df = pd.DataFrame({"x": [1, 1, 2, 3], "y": [4, 4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df)
    
    assert duplicates_counter == Counter({(1, 4): 2})
    assert len(unique_df) == 3
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].tolist() == [0, 0, 0]

def test_task_func_with_fewer_unique_points_than_clusters(mock_kmeans):
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=3)
    
    assert duplicates_counter == Counter()
    assert len(unique_df) == 2
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].tolist() == [0, 0]

def test_task_func_with_random_state(mock_kmeans):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    _, _, _ = task_func(df, random_state=42)

def test_task_func_with_n_init(mock_kmeans):
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    _, _, _ = task_func(df, n_init=5)