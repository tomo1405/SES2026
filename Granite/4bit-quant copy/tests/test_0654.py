import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(dataframe, target_value='332'):
    mask = dataframe.applymap(lambda x: x == target_value)

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(mask, cmap='Blues', cbar=False)  # Adjusted to not display color bar for clarity in Boolean visualization
    plt.show()

    return mask, ax

def test_task_func():
    # Mock the input dataframe
    dataframe = ...

    # Call the function
    mask, ax = task_func(dataframe)

    # Assert the expected output
    assert isinstance(mask, ...)
    assert isinstance(ax, ...)
    assert ax.get_xlabel() == 'Columns'
    assert ax.get_ylabel() == 'Rows'
    assert ax.get_title() == 'Heatmap of Mask'