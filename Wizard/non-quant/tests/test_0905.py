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

# Test case 1
d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
keys = ['x', 'y']
ax = task_func(d, keys)
assert ax.get_xlabel() == 'x'
assert ax.get_ylabel() == 'y'
assert ax.get_title() == ''
assert ax.get_legend().get_texts()[0].get_text() == 'x'
assert ax.get_legend().get_texts()[1].get_text() == 'y'
assert ax.get_legend().get_texts()[2].get_text() == 'z'
assert ax.lines[0].get_xdata().tolist() == [0, 1]
assert ax.lines[0].get_ydata().tolist() == [1, 2]
assert ax.lines[1].get_xdata().tolist() == [0, 1]
assert ax.lines[1].get_ydata().tolist() == [4, 5]

# Test case 2
d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
keys = ['x', 'y', 'z']
ax = task_func(d, keys)
assert ax.get_xlabel() == 'x'
assert ax.get_ylabel() == 'y'
assert ax.get_title() == ''
assert ax.get_legend().get_texts()[0].get_text() == 'x'
assert ax.get_legend().get_texts()[1].get_text() == 'y'
assert ax.get_legend().get_texts()[2].get_text() == 'z'
assert ax.lines[0].get_xdata().tolist() == [0, 1]
assert ax.lines[0].get_ydata().tolist() == [1, 2]
assert ax.lines[1].get_xdata().tolist() == [0, 1]
assert ax.lines[1].get_ydata().tolist() == [4, 5]
assert ax.lines[2].get_xdata().tolist() == [0, 1]
assert ax.lines[2].get_ydata().tolist() == [3, 6]

# Test case 3
d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
keys = ['x', 'y', 'w']
ax = task_func(d, keys)
assert ax.get_xlabel() == 'x'
assert ax.get_ylabel() == 'y'
assert ax.get_title() == ''
assert ax.get_legend().get_texts()[0].get_text() == 'x'
assert ax.get_legend().get_texts()[1].get_text() == 'y'
assert ax.get_legend().get_texts()[2].get_text() == 'z'
assert ax.lines[0].get_xdata().tolist() == [0, 1]
assert ax.lines[0].get_ydata().tolist() == [1, 2]
assert ax.lines[1].get_xdata().tolist() == [0, 1]
assert ax.lines[1].get_ydata().tolist() == [4, 5]
assert ax.lines[2].get_xdata().tolist() == []
assert ax.lines[2].get_ydata().tolist() == []

# Test case 4
d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
keys = []
ax = task_func(d, keys)
assert ax.get_xlabel() == 'x'
assert ax.get_ylabel() == 'y'
assert ax.get_title() == ''
assert ax.get_legend().get_texts()[0].get_text() == 'x'
assert ax.get_legend().get_texts()[1].get_text() == 'y'
assert ax.get_legend().get_texts()[2].get_text() == 'z'
assert ax.lines[0].get_xdata().tolist() == []
assert ax.lines[0].get_ydata().tolist() == []
assert ax.lines[1].get_xdata().tolist() == []
assert ax.lines[1].get_ydata().tolist() == []
assert ax.lines[2].get_xdata().tolist() == []
assert ax.lines[2].get_ydata().tolist() == []

# Test case 5
d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
keys = ['x', 'y', 'w']
with pytest.raises(KeyError):
    task_func(d, keys)