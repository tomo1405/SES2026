import io
import sys

import matplotlib.pyplot as plt
import pandas as pd
from src_0920 import task_func


def capture_plot(ax):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

def test_task_func():
    data = {'category': ['A', 'B', 'A', 'C', 'A', 'B', 'D', 'E']}
    column = 'category'
    
    # Capture stdout to suppress plot display
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ax = task_func(data, column)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the plot is generated correctly
    buf = capture_plot(ax)
    assert buf.getvalue() != b'', "The plot should be generated and saved to the buffer."
    
    # Check if the DataFrame is processed correctly
    expected_counts = pd.Series({'A': 3, 'B': 2, 'C': 1, 'D': 1, 'E': 1})
    actual_counts = pd.Series(ax.get_ydata(), index=ax.get_xticklabels())
    pd.testing.assert_series_equal(actual_counts, expected_counts)

def test_task_func_missing_categories():
    data = {'category': ['A', 'B', 'A', 'C', 'A', 'B']}
    column = 'category'
    
    # Capture stdout to suppress plot display
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ax = task_func(data, column)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the plot is generated correctly
    buf = capture_plot(ax)
    assert buf.getvalue() != b'', "The plot should be generated and saved to the buffer."
    
    # Check if the DataFrame is processed correctly with missing categories
    expected_counts = pd.Series({'A': 3, 'B': 2, 'C': 1, 'D': 0, 'E': 0})
    actual_counts = pd.Series(ax.get_ydata(), index=ax.get_xticklabels())
    pd.testing.assert_series_equal(actual_counts, expected_counts)