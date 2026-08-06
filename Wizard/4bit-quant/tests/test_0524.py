python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    if not data:
        return None
    df = pd.DataFrame(data)
    plt.figure()
    for label in df.columns:
        plt.plot(df[label], label=label)
    plt.xlabel("Time")
    plt.ylabel("Data Points")
    plt.title("Data over Time")
    return plt.gca()

def test_task_func():
    # Test case 1: data is empty
    assert task_func([]) is None
    
    # Test case 2: data is not empty
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Data Points'
    assert ax.get_title() == 'Data over Time'
    assert ax.get_legend_handles_labels()[0] == list(data.keys())
    assert ax.get_legend_handles_labels()[1] == list(data.values())