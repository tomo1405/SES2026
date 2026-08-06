import pytest
from src_0052 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        "Age": [25, 30, 35, 40, 45],
        "Height": [160, 170, 180, 190, 200]
    }
    return pd.DataFrame(data)

def test_task_func_no_clusters(sample_df):
    age = 40
    height = 170
    result_df, ax = task_func(sample_df, age, height)
    assert result_df["Cluster"].nunique() == 1
    assert ax is None

def test_task_func_with_clusters(sample_df):
    age = 20
    height = 210
    result_df, ax = task_func(sample_df, age, height)
    assert result_df["Cluster"].nunique() == 3
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_df(sample_df):
    age = 50
    height = 150
    result_df, ax = task_func(sample_df, age, height)
    assert result_df.empty
    assert ax is None

def test_task_func_edge_case(sample_df):
    age = 35
    height = 180
    result_df, ax = task_func(sample_df, age, height)
    assert result_df["Cluster"].nunique() == 1
    assert ax is None