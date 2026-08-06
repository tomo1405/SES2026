import pytest
from src_0010 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    # Test data
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    expected_df = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [10, 20, 30]})
    
    # Call the function
    result_df, ax = task_func(list_of_pairs)
    
    # Check the DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check the plot
    assert plt.gca() == ax

    # Close the plot to avoid displaying the plot in the console
    plt.close()