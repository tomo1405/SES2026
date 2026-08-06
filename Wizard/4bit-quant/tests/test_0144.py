python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func():
    X = np.linspace(-10, 10, 400)  # X range specified
    y = 2 * X + 1

    fig, ax = plt.subplots()
    ax.plot(X, y, '-r', label='y=2x+1')
    
    solution_y = 2 * 2 + 1  # y value at x = 2
    ax.plot(2, solution_y, 'go', label='Solution at x=2')
    
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim([-10, 10])  # Explicitly setting the x-axis range
    # ax.set_ylim is optional and can be set if a specific y-range is desired
    ax.legend(loc='best')
    ax.grid()

    return ax

def test_task_func():
    ax = task_func()
    assert ax.get_title() == 'Solution of the equation y=2x+1 at x=2'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_xlim() == (-10, 10)
    # assert ax.get_ylim() == (0, 10)  # Optional assertion
    assert ax.get_legend().get_texts()[0].get_text() == 'y=2x+1'
    assert ax.get_legend().get_texts()[1].get_text() == 'Solution at x=2'
    assert ax.get_gridlines()[0].get_linestyle() == '--'