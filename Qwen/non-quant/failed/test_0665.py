import pytest
from src_0665 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def sample_sales_data():
    data = io.StringIO("""
Month,A,B,C
Jan,100,150,200
Feb,110,160,210
Mar,120,170,220
Apr,130,180,230
May,140,190,240
""")
    return pd.read_csv(data)

def test_task_func(sample_sales_data):
    ax = task_func(sample_sales_data)
    
    # Check if the plot is created with the correct number of lines
    assert len(ax.lines) == 3  # One line per product (excluding 'Month' column)
    
    # Check if the fill_between areas are created
    assert len(ax.collections) == 3  # One fill_between per product
    
    # Check if the x-axis and y-axis labels are set correctly
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Sales'
    
    # Check if the title is set correctly
    assert ax.get_title() == 'Monthly Sales Trends with Standard Deviation'
    
    # Check if the legend is present
    assert ax.get_legend() is not None
    
    # Check if the x-ticks are set correctly
    expected_xticks = sample_sales_data['Month'].tolist()
    assert list(ax.get_xticks()) == expected_xticks

    # Check if the plot contains the correct data points
    for i, label in enumerate(sample_sales_data.columns[1:]):
        line = ax.lines[i]
        xdata, ydata = line.get_data()
        np.testing.assert_array_equal(xdata, sample_sales_data['Month'])
        np.testing.assert_array_equal(ydata, sample_sales_data[label])

# To run the tests, you can use the following command in your terminal:
# pytest <filename>.py