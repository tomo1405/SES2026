python
import pytest
from src_0052 import task_func
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Valid input, 3 clusters
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = 175
    selected_df, ax = task_func(df, age, height)
    assert selected_df.shape == (2, 3)
    assert selected_df["Cluster"].tolist() == [1, 1]
    assert ax is not None

    # Test case 2: Valid input, 2 clusters
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = 185
    selected_df, ax = task_func(df, age, height)
    assert selected_df.shape == (3, 3)
    assert selected_df["Cluster"].tolist() == [1, 1, 2]
    assert ax is not None

    # Test case 3: Valid input, 1 cluster
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = 205
    selected_df, ax = task_func(df, age, height)
    assert selected_df.shape == (5, 3)
    assert selected_df["Cluster"].tolist() == [1, 1, 1, 1, 1]
    assert ax is not None

    # Test case 4: Invalid input, age is not an integer
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = "30"
    height = 175
    with pytest.raises(TypeError):
        selected_df, ax = task_func(df, age, height)

    # Test case 5: Invalid input, height is not an integer
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = "175"
    with pytest.raises(TypeError):
        selected_df, ax = task_func(df, age, height)

    # Test case 6: Invalid input, age is negative
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = -30
    height = 175
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, age, height)

    # Test case 7: Invalid input, height is negative
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = -175
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, age, height)

    # Test case 8: Invalid input, age is greater than 100
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 130
    height = 175
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, age, height)

    # Test case 9: Invalid input, height is greater than 250
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 30
    height = 275
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, age, height)

    # Test case 10: Invalid input, no rows in the filtered DataFrame
    df = pd.DataFrame({"Age": [25, 30, 35, 40, 45], "Height": [160, 170, 180, 190, 200]})
    age = 50
    height = 175
    selected_df, ax = task_func(df, age, height)
    assert selected_df.shape == (0, 3)
    assert selected_df["Cluster"].tolist() == []
    assert ax is None