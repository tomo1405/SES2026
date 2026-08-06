import pytest
from src_0532 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'x': [1, 2, 2, 3, 4, 4, 5],
        'y': [1, 2, 2, 3, 4, 4, 5]
    }
    return pd.DataFrame(data)

def test_task_func_with_no_duplicates(sample_data):
    duplicates_counter, unique_df, ax = task_func(sample_data, n_clusters=3)
    assert duplicates_counter == Counter(), "There should be no duplicates"
    assert len(unique_df) == len(sample_data), "All data points should be unique"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

def test_task_func_with_duplicates(sample_data):
    # Introduce duplicates
    sample_data.loc[len(sample_data)] = [2, 2]  # Adding a duplicate point (2, 2)
    duplicates_counter, unique_df, ax = task_func(sample_data, n_clusters=3)
    assert duplicates_counter == Counter({(2, 2): 2}), "There should be one duplicate point (2, 2)"
    assert len(unique_df) == len(sample_data) - 1, "One duplicate should be removed"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

def test_task_func_with_fewer_unique_points_than_clusters(sample_data):
    # Reduce the number of unique points
    sample_data = sample_data.head(2)
    duplicates_counter, unique_df, ax = task_func(sample_data, n_clusters=3)
    assert duplicates_counter == Counter(), "There should be no duplicates"
    assert len(unique_df) == 2, "There should be only 2 unique points"
    assert len(unique_df['cluster'].unique()) == 2, "Number of clusters should match the number of unique points"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

def test_task_func_with_random_state(sample_data):
    duplicates_counter1, unique_df1, _ = task_func(sample_data, n_clusters=3, random_state=42)
    duplicates_counter2, unique_df2, _ = task_func(sample_data, n_clusters=3, random_state=42)
    assert duplicates_counter1 == duplicates_counter2, "Duplicate counters should be the same"
    assert unique_df1.equals(unique_df2), "Unique dataframes should be the same"