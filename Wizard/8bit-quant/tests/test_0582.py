python
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    
    return ax

# Test the function
def test_task_func():
    # Test the default values
    ax = task_func()
    assert ax.get_title() == 'Plot of sin(x)'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'sin(x)'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()) == 2
    assert ax.lines[0].get_data()[0].shape == (SIZE,)
    assert ax.lines[0].get_data()[1].shape == (SIZE,)
    
    # Test the custom values
    ax = task_func(size=500, frequency=2)
    assert ax.get_title() == 'Plot of sin(x)'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'sin(x)'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()) == 2
    assert ax.lines[0].get_data()[0].shape == (500,)
    assert ax.lines[0].get_data()[1].shape == (500,)

test_task_func()