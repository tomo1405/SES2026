import matplotlib.pyplot as plt
import numpy as np
import pytest

def task_func(myList):
    _, ax = plt.subplots()
    ax.hist(
        myList, bins=np.arange(min(myList), max(myList) + 2) - 0.5, edgecolor="black"
    )
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Values")
    return ax

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    ax = task_func(myList)
    assert ax is not None
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Values"