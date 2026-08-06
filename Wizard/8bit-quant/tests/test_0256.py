python
import matplotlib
import numpy as np
import pytest

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    print(type(ax))
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("The input is not an axes")
    x = np.linspace(0, 2 * np.pi, 1000)
    y = FUNCTIONS[func_index](x)

    ax.plot(x, y)
    ax.set_rlabel_position(func_index * 45)
    return ax

def test_task_func():
    # Test case 1: Valid input
    fig, ax = plt.subplots()
    task_func(ax, 0)
    plt.close()

    # Test case 2: Invalid input
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        task_func(ax, 3)
    plt.close()