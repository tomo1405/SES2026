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

# Test the function with some sample data
def test_task_func():
    data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9}
    ]
    ax = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'z'
    assert len(ax.lines) == 3
    assert ax.lines[0].get_label() == 'x'
    assert ax.lines[1].get_label() == 'y'
    assert ax.lines[2].get_label() == 'z'
    assert ax.lines[0].get_xydata().shape == (3, 2)
    assert ax.lines[1].get_xydata().shape == (3, 2)
    assert ax.lines[2].get_xydata().shape == (3, 2)
    assert ax.lines[0].get_xydata()[0][0] == 1
    assert ax.lines[0].get_xydata()[0][1] == 2
    assert ax.lines[0].get_xydata()[1][0] == 4
    assert ax.lines[0].get_xydata()[1][1] == 5
    assert ax.lines[0].get_xydata()[2][0] == 7
    assert ax.lines[0].get_xydata()[2][1] == 8
    assert ax.lines[1].get_xydata()[0][0] == 1
    assert ax.lines[1].get_xydata()[0][1] == 2
    assert ax.lines[1].get_xydata()[1][0] == 4
    assert ax.lines[1].get_xydata()[1][1] == 5
    assert ax.lines[1].get_xydata()[2][0] == 7
    assert ax.lines[1].get_xydata()[2][1] == 8
    assert ax.lines[2].get_xydata()[0][0] == 1
    assert ax.lines[2].get_xydata()[0][1] == 2
    assert ax.lines[2].get_xydata()[1][0] == 4
    assert ax.lines[2].get_xydata()[1][1] == 5
    assert ax.lines[2].get_xydata()[2][0] == 7
    assert ax.lines[2].get_xydata()[2][1] == 8
    assert ax.get_legend().texts[0].get_text() == 'x'
    assert ax.get_legend().texts[1].get_text() == 'y'
    assert ax.get_legend().texts[2].get_text() == 'z'

# Run the test
test_task_func()