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
    assert isinstance(ax, plt.Axes)  # Check if the returned object is an Axes instance
    lines = ax.get_lines()
    assert len(lines) == 3  # Check if the correct number of lines are plotted
    x_values = [line.get_xdata() for line in lines]
    y_values = [line.get_ydata() for line in lines]
    assert x_values == [1, 4, 7]  # Check if the x-values are correct
    assert y_values == [2, 5, 8]  # Check if the y-values are correct

if __name__ == '__main__':
    pytest.main()