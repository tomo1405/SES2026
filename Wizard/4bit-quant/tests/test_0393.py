python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytest

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col, group_name):
    # Filter the DataFrame to select the specific group
    group_data = df[df[group_col] == group_name]
    if group_data.empty:
        raise ValueError
    
    # Create a figure and axes
    fig, ax = plt.subplots()

    # Get the number of bars
    num_bars = len(group_data)

    # Set the width of the bars
    bar_width = 0.35

    # Generate positions for the bars
    index = np.arange(num_bars)

    # Create the bar chart
    bars = ax.bar(index, group_data[value_col], bar_width, color=COLORS[:num_bars])

    # Set labels and title
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    ax.set_title(f'Bar chart of {value_col} for {group_name}')

    # Set x-axis ticks and labels
    ax.set_xticks(index)
    ax.set_xticklabels(group_data[group_col])

    return ax

# Test case 1: valid input
df = pd.DataFrame({'group': ['A', 'B', 'C'], 'value': [10, 20, 30]})
group_col = 'group'
value_col = 'value'
group_name = 'B'
ax = task_func(df, group_col, value_col, group_name)
assert ax.get_xlabel() == group_col
assert ax.get_ylabel() == value_col
assert ax.get_title().get_text() == f'Bar chart of {value_col} for {group_name}'
assert ax.get_xticks() == [0, 1, 2]
assert ax.get_xticklabels() == ['A', 'B', 'C']
assert ax.patches[0].get_height() == 20
assert ax.patches[1].get_height() == 30
assert ax.patches[2].get_height() == 0

# Test case 2: invalid input (empty DataFrame)
df = pd.DataFrame({'group': [], 'value': []})
group_col = 'group'
value_col = 'value'
group_name = 'B'
with pytest.raises(ValueError):
    ax = task_func(df, group_col, value_col, group_name)

# Test case 3: invalid input (group name not in DataFrame)
df = pd.DataFrame({'group': ['A', 'B', 'C'], 'value': [10, 20, 30]})
group_col = 'group'
value_col = 'value'
group_name = 'D'
with pytest.raises(ValueError):
    ax = task_func(df, group_col, value_col, group_name)