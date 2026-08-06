python
import math
import random
import matplotlib.pyplot as plt
import pytest

def task_func():
    x = [i/100 for i in range(1000)]
    frequency = random.randint(1, 5)
    amplitude = random.randint(1, 5)
    phase_shift = random.randint(0, 360)

    y = [amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)) for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    
    return ax  # Return the axis object for testing

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)  # Check if the returned object is an Axes object
    assert ax.get_title() == 'Random Sine Wave'  # Check if the title is correct
    assert ax.get_xlabel() == 'Time'  # Check if the xlabel is correct
    assert ax.get_ylabel() == 'Amplitude'  # Check if the ylabel is correct
    assert ax.get_xlim() == (0, 1)  # Check if the xlim is correct
    assert ax.get_ylim() == (-5, 5)  # Check if the ylim is correct
    assert ax.get_gridlines()[0].get_linestyle() == '--'  # Check if the gridline style is correct
    assert ax.get_gridlines()[0].get_color() == 'gray'  # Check if the gridline color is correct