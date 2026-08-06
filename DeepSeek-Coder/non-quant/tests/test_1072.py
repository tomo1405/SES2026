import pytest
from src_1072 import task_func
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
from random import shuffle

def test_task_func():
    # Create a sample list of lists for testing
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Call the function
    fig, ax = task_func(list_of_lists)

    # Assertions to check the output
    assert fig is not None
    assert ax is not None
    assert len(ax.lines) == len(list_of_lists)

    # Close the figure to avoid memory leaks
    plt.close(fig)