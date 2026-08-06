import pytest
from src_1034 import task_func

def test_task_func():
    df, ax = task_func()

    # Test that the returned objects are not None
    assert df is not None
    assert ax is not None

    # Test that the DataFrame has the correct shape and columns
    assert df.shape == (52, 3)
    assert list(df.columns) == ["a", "b", "c"]

    # Test that the value counts are correct
    value_counts = df["a"].value_counts()
    assert value_counts.shape == (26,)
    assert list(value_counts.index) == list(string.ascii_lowercase)
    assert value_counts.sum() == 52

    # Test that the histogram plot is correct
    assert ax.get_xlabel() == "Letter"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Letter Value Counts"