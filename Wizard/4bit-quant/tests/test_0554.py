python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(a, b):
    if not a or not b:  # Check if either list is empty
        fig, ax = plt.subplots()  # Creates a blank plot
        plt.close(fig)  # Close the plot window to prevent it from showing empty plots
        return ax

    # Use np.random.seed for reproducibility if needed
    np.random.seed(0)
    # Ensure column names from b are used only up to the length of b
    selected_columns = COLUMNS[:len(b)]
    df = pd.DataFrame(np.random.randn(len(a), len(b)), index=a, columns=selected_columns)
    ax = df.plot(kind='bar')
    plt.show()
    return ax

def test_task_func():
    # Test case 1: a and b are empty lists
    a = []
    b = []
    ax = task_func(a, b)
    assert ax is None
    
    # Test case 2: a and b are non-empty lists
    a = ['a', 'b', 'c']
    b = ['B', 'C']
    ax = task_func(a, b)
    assert isinstance(ax, plt.Axes)