python
import numpy as np
import matplotlib.pyplot as plt
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

# Test the function with a sample DataFrame
df = pd.DataFrame({'group': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'value': [10, 20, 30, 40, 50, 60]})

# Test with group_name 'A'
ax = task_func(df, 'group', 'value', 'A')
assert ax.get_title() == 'Bar chart of value for A'
assert ax.get_xlabel() == 'group'
assert ax.get_ylabel() == 'value'
assert ax.get_xticks() == [0, 2, 4]
assert ax.get_xticklabels() == ['A', 'C', 'A']
assert ax.get_yticks() == [0, 10, 20, 30, 40, 50, 60]
assert ax.get_ylim() == (0, 60)
assert ax.patches[0].get_facecolor() == (1.0, 0.0, 0.0, 1.0)
assert ax.patches[1].get_facecolor() == (0.0, 0.0, 1.0, 1.0)
assert ax.patches[2].get_facecolor() == (0.0, 1.0, 0.0, 1.0)

# Test with group_name 'B'
ax = task_func(df, 'group', 'value', 'B')
assert ax.get_title() == 'Bar chart of value for B'
assert ax.get_xlabel() == 'group'
assert ax.get_ylabel() == 'value'
assert ax.get_xticks() == [1, 3, 5]
assert ax.get_xticklabels() == ['B', 'C', 'B']
assert ax.get_yticks() == [0, 10, 20, 30, 40, 50, 60]
assert ax.get_ylim() == (0, 60)
assert ax.patches[0].get_facecolor() == (0.0, 0.0, 1.0, 1.0)
assert ax.patches[1].get_facecolor() == (0.0, 1.0, 0.0, 1.0)
assert ax.patches[2].get_facecolor() == (1.0, 0.0, 0.0, 1.0)

# Test with group_name 'C'
ax = task_func(df, 'group', 'value', 'C')
assert ax.get_title() == 'Bar chart of value for C'
assert ax.get_xlabel() == 'group'
assert ax.get_ylabel() == 'value'
assert ax.get_xticks() == [0, 2, 4]
assert ax.get_xticklabels() == ['A', 'C', 'A']
assert ax.get_yticks() == [0, 10, 20, 30, 40, 50, 60]
assert ax.get_ylim() == (0, 60)
assert ax.patches[0].get_facecolor() == (0.0, 1.0, 0.0, 1.0)
assert ax.patches[1].get_facecolor() == (1.0, 0.0, 0.0, 1.0)
assert ax.patches[2].get_facecolor() == (0.0, 0.0, 1.0, 1.0)

# Test with an invalid group_name
with pytest.raises(ValueError):
    task_func(df, 'group', 'value', 'D')