import pytest
from src_0338 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value': [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    ax = task_func(sample_df, 'group', 'value')
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the correct number of bars are plotted
    bars = ax.patches
    assert len(bars) == 3, "There should be 3 bars, one for each group"
    
    # Check if the correct colors are used
    expected_colors = ['r', 'g', 'b']
    for i, bar in enumerate(bars):
        assert bar.get_facecolor() == expected_colors[i], f"Bar {i+1} should have color {expected_colors[i]}"
    
    # Check if the correct labels are set
    assert ax.get_xlabel() == 'group'
    assert ax.get_ylabel() == 'value'
    assert ax.get_title() == 'Bar chart of value by group'
    
    # Check if the x-axis labels are set correctly
    xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
    assert xtick_labels == ['A', 'B', 'C'], "X-axis labels should be ['A', 'B', 'C']"

# To run the tests, you can use the following command in your terminal:
# pytest -v