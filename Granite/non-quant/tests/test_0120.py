import matplotlib.pyplot as plt
from src_0120 import task_func


def test_task_func():
    # Call the function
    task_func()

    # Use pytest's assertion to check if the figure is created
    assert plt.fignum_exists(0)

    # Check if the title, xlabel, ylabel, and grid are set correctly
    fig = plt.figure(0)
    assert fig.axes[0].get_title() == 'y = x^2'
    assert fig.axes[0].get_xlabel() == 'x'
    assert fig.axes[0].get_ylabel() == 'y'
    assert fig.axes[0].gridOn