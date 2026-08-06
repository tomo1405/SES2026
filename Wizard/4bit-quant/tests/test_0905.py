python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(d, keys=['x', 'y', 'z']):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)

    # Initialize a plot
    fig, ax = plt.subplots()
    
    # Plot the values for the specified keys
    plotted_keys = []
    for key in keys:
        if key in df.columns:
            ax.plot(df[key], label=key)
            plotted_keys.append(key)
    
    # Add a legend if there are any lines plotted
    if plotted_keys:
        ax.legend()
    
    # Return the Axes object
    return ax

def test_task_func():
    # Test case 1: Test with valid data
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(d)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'z'
    assert ax.get_legend_handles_labels()[0] == ['x', 'y', 'z']
    assert ax.get_legend_handles_labels()[1] == ['x', 'y', 'z']
    
    # Test case 2: Test with missing data
    d = [{'x': 1, 'y': 2}, {'x': 4, 'y': 5, 'z': 6}]
    ax = task_func(d)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'z'
    assert ax.get_legend_handles_labels()[0] == ['x', 'y']
    assert ax.get_legend_handles_labels()[1] == ['x', 'y', 'z']
    
    # Test case 3: Test with empty data
    d = []
    ax = task_func(d)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''
    assert ax.get_title() == ''
    assert ax.get_legend_handles_labels()[0] == []
    assert ax.get_legend_handles_labels()[1] == []