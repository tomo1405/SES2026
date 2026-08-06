python
import numpy as np
import matplotlib.pyplot as plt
import pytest

# Constants
ARRAY_SIZE = 10000

def task_func():
    array = np.random.randint(1, 100, size=ARRAY_SIZE)
    mean = np.mean(array)
    std = np.std(array)

    fig, ax = plt.subplots()
    ax.hist(array, bins='auto')
    ax.set_title('Histogram of Random Integers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.axvline(mean, color='red', linestyle='dashed', linewidth=1)
    ax.axvline(mean + std, color='purple', linestyle='dashed', linewidth=1)
    ax.axvline(mean - std, color='purple', linestyle='dashed', linewidth=1)
    ax.legend(["Mean", "Standard Deviation"])
    plt.show()
    
    return array, mean, std, ax

def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, plt.Axes)