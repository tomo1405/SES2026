python
import pytest
from src_0532 import task_func

def test_task_func():
    # Test case 1: n_clusters is greater than number of unique data points
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=6)
    assert len(unique_df["cluster"].unique()) == 5

    # Test case 2: n_clusters is less than number of unique data points
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2)
    assert len(unique_df["cluster"].unique()) == 2

    # Test case 3: n_clusters is equal to number of unique data points
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5)
    assert len(unique_df["cluster"].unique()) == 5

    # Test case 4: n_clusters is equal to number of unique data points and there are no duplicates
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 0

    # Test case 5: n_clusters is greater than number of unique data points and there are duplicates
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=6)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 6: n_clusters is less than number of unique data points and there are duplicates
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2)
    assert len(unique_df["cluster"].unique()) == 2
    assert len(duplicates_counter) == 5

    # Test case 7: n_clusters is equal to number of unique data points and there are duplicates
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 8: n_clusters is equal to number of unique data points and there are duplicates and n_init is 1
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, n_init=1)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 9: n_clusters is equal to number of unique data points and there are duplicates and n_init is 2
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, n_init=2)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 10: n_clusters is equal to number of unique data points and there are duplicates and random_state is set
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, random_state=42)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 11: n_clusters is equal to number of unique data points and there are duplicates and random_state is set and n_init is 1
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, random_state=42, n_init=1)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5

    # Test case 12: n_clusters is equal to number of unique data points and there are duplicates and random_state is set and n_init is 2
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, random_state=42, n_init=2)
    assert len(unique_df["cluster"].unique()) == 5
    assert len(duplicates_counter) == 5