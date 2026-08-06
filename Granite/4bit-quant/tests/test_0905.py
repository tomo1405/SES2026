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
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]
    ax = task_func(d)
    assert isinstance(ax, plt.Axes)
    assert ax.get_legend() is not None
    assert ax.get_legend().get_texts()[0].get_text() in ['x', 'y', 'z']

def test_task_func_with_invalid_keys():
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]
    with pytest.raises(ValueError):
        task_func(d, keys=['a', 'b', 'c'])

def test_task_func_with_no_keys():
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]
    ax = task_func(d, keys=[])
    assert ax.get_legend() is None