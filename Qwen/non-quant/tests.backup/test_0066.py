import pytest
from src_0066 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 3],
        [2, 2, 3],
        [2, 2, 4]
    ]

def test_task_func_output(sample_data):
    analyzed_df, ax = task_func(sample_data)
    
    # Check if the DataFrame is correctly analyzed
    expected_df = pd.DataFrame({
        'col1': [1, 1, 2, 2],
        'col2': [2, 3, 2, 2],
        'col3': [2, 1, 1, 2]
    })
    pd.testing.assert_frame_equal(analyzed_df.reset_index(drop=True), expected_df)

    # Check if the plot is created with the correct labels
    assert ax.get_xlabel() == 'col1-col2'
    assert ax.get_ylabel() == 'col3'

def test_task_func_plot_data(sample_data):
    analyzed_df, ax = task_func(sample_data)
    
    # Check if the plot data matches the analyzed DataFrame
    x_data = analyzed_df[['col1', 'col2']].astype(str).agg('-'.join, axis=1)
    y_data = analyzed_df['col3']
    lines = ax.get_lines()
    assert len(lines) == 1
    plotted_x_data = lines[0].get_xdata()
    plotted_y_data = lines[0].get_ydata()
    assert all(plotted_x_data == x_data)
    assert all(plotted_y_data == y_data)

def test_task_func_empty_data():
    analyzed_df, ax = task_func([])
    
    # Check if the DataFrame is empty
    assert analyzed_df.empty
    
    # Check if the plot is created with the correct labels
    assert ax.get_xlabel() == 'col1-col2'
    assert ax.get_ylabel() == 'col3'
    assert len(ax.get_lines()) == 0