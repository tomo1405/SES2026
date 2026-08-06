import pytest
from src_0532 import task_func

def test_task_func():
    # Test with a sample dataframe
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
    duplicates_counter, unique_df, ax = task_func(df)

    # Test that duplicates are correctly identified
    assert duplicates_counter == Counter({(1, 1): 1, (2, 2): 1, (3, 3): 1, (4, 4): 1, (5, 5): 1})

    # Test that unique data points are correctly clustered
    assert unique_df["cluster"].value_counts().sort_index().equals(pd.Series([1, 2, 3, 4, 5], index=[0, 1, 2, 3, 4]))

    # Test that the plot is correctly generated
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"

    # Test that the function returns the correct number of clusters
    assert len(unique_df["cluster"].unique()) == 5

    # Test that the function returns the correct number of duplicates
    assert len(duplicates_counter) == 5