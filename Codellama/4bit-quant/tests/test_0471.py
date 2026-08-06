import pytest
from src_0471 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    ax = task_func(myList)
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Values"
    assert ax.get_xlim() == (min(myList), max(myList) + 2)
    assert ax.get_ylim() == (0, len(myList))
    assert ax.get_xticks() == np.arange(min(myList), max(myList) + 2) - 0.5
    assert ax.get_yticks() == np.arange(len(myList))
    assert ax.get_xticklabels() == [str(i) for i in np.arange(min(myList), max(myList) + 2) - 0.5]
    assert ax.get_yticklabels() == [str(i) for i in np.arange(len(myList))]
    assert ax.get_edgecolor() == "black"
    plt.close(ax.figure)