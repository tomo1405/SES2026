import pytest
from src_0532 import task_func

def test_task_func():
    # Test case 1: Test that duplicates are identified correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 2, 3, 4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=3, random_state=None, n_init=10)
    assert duplicates_counter == Counter({(1, 1): 1, (2, 2): 1, (3, 3): 1, (4, 4): 1, (5, 5): 1, (6, 6): 1})

    # Test case 2: Test that KMeans clustering is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 2, 3, 4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=3, random_state=None, n_init=10)
    assert unique_df["cluster"].value_counts().sort_index() == [1, 1, 1, 2, 2, 2]

    # Test case 3: Test that plotting is performed correctly
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 2, 3, 4, 5, 6]})
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=3, random_state=None, n_init=10)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"
    assert len(ax.get_lines()) == 1
    assert len(ax.get_patches()) == 3