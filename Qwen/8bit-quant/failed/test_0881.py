import pytest
from src_0881 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    # Create a valid DataFrame with numeric values
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    labels, kmeans = task_func(data, n_clusters=2, seed=0)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(data)
    assert isinstance(kmeans, KMeans)

def test_task_func_with_non_numeric_data():
    # Create a DataFrame with non-numeric values
    data = pd.DataFrame({
        'A': [1, 2, 'a', 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data, n_clusters=2, seed=0)

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    data = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data, n_clusters=2, seed=0)

def test_task_func_with_single_column():
    # Create a DataFrame with a single column
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5]
    })
    labels, kmeans = task_func(data, n_clusters=2, seed=0)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(data)
    assert isinstance(kmeans, KMeans)

def test_task_func_with_all_zeroes():
    # Create a DataFrame with all zeroes
    data = pd.DataFrame({
        'A': [0, 0, 0, 0, 0],
        'B': [0, 0, 0, 0, 0]
    })
    labels, kmeans = task_func(data, n_clusters=2, seed=0)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(data)
    assert isinstance(kmeans, KMeans)