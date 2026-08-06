import pytest
from src_0010 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    # Test with a simple list of pairs
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    df, ax = task_func(list_of_pairs)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [10, 20, 30]})
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot title is set correctly
    assert ax.get_title() == "Category vs Value"
    
    # Check if the x-axis label is set correctly
    assert ax.get_xlabel() == "Category"
    
    # Check if the y-axis label is set correctly
    assert ax.get_ylabel() == "Value"
    
    # Check if the number of bars in the plot is correct
    bars = ax.patches
    assert len(bars) == 3
    
    # Check if the values of the bars are correct
    for i, bar in enumerate(bars):
        assert bar.get_height() == expected_df.iloc[i]["Value"]

# To run the tests, you can use the following command:
# pytest -v