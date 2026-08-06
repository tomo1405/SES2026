import pytest
from src_1025 import task_func
import numpy as np
import pandas as pd
import seaborn as sns

# Constants
PLOT_TITLE = "Value Distribution"

def test_task_func():
    # Test case 1: Normal case
    data_dict = {'col1': [1, 2, 3, 4, 5]}
    expected_df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
    expected_plot = sns.histplot([1, 2, 3, 4, 5], bins=5, kde=False)
    expected_plot.set_title(PLOT_TITLE)
    
    df, plot = task_func(data_dict)
    
    assert df.equals(expected_df)
    assert plot.get_title() == PLOT_TITLE

    # Add more test cases as needed

# Add more test cases as needed