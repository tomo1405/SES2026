import pytest
from src_0532 import task_func

def test_task_func():
    # Test case 1: Test that duplicates are identified correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert unique_df.equals(df)

    # Test case 2: Test that KMeans clustering is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2)
    assert duplicates_counter == Counter()
    assert unique_df.equals(df)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

    # Test case 3: Test that duplicates are removed and KMeans clustering is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2, random_state=42)
    assert duplicates_counter == Counter()
    assert unique_df.equals(df)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

    # Test case 4: Test that duplicates are removed and KMeans clustering is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2, n_init=10)
    assert duplicates_counter == Counter()
    assert unique_df.equals(df)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

    # Test case 5: Test that duplicates are removed and KMeans clustering is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=2, random_state=42, n_init=10)
    assert duplicates_counter == Counter()
    assert unique_df.equals(df)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"