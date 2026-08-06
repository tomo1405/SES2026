import pytest
from src_0010 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of pairs
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    df, ax = task_func(list_of_pairs)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame(list_of_pairs, columns=["Category", "Value"])
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Category vs Value"
    assert len(ax.patches) == 3  # There should be one bar for each pair

# To run the tests, use the command: pytest <filename>.py