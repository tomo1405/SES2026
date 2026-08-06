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
    expected_df = pd.DataFrame({
        "Category": ["A", "B", "C"],
        "Value": [10, 20, 30]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Category vs Value"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Value"
    
    # Check if the barplot has the correct number of bars
    bars = ax.patches
    assert len(bars) == 3  # There should be 3 bars for each category
    
    # Check if the values on the y-axis are correct
    y_values = [bar.get_height() for bar in bars]
    assert y_values == [10, 20, 30]

# Run the tests
if __name__ == "__main__":
    pytest.main()