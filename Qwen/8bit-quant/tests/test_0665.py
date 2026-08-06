import pytest
from src_0665 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

# Mock data for testing
data = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'ProductA': [100, 150, 200],
    'ProductB': [120, 180, 240]
}
sales_data = pd.DataFrame(data)

def test_task_func():
    ax = task_func(sales_data)
    
    # Check if the plot is created
    assert isinstance(ax, plt.AxesSubplot)
    
    # Check if the correct number of lines are plotted
    lines = ax.get_lines()
    assert len(lines) == 2  # One line per product
    
    # Check if the labels are set correctly
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    
    # Check if the legend is present
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert set(legend_labels) == {'ProductA', 'ProductB'}
    
    # Check if the x-ticks are set correctly
    xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
    assert set(xtick_labels) == {'Jan', 'Feb', 'Mar'}

# Run the tests
if __name__ == "__main__":
    pytest.main()