import pytest
from src_0477 import task_func
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def test_task_func():
    # Create dummy data
    X = [1, 2, 3, 4, 5]
    Y = [2, 3, 5, 7, 11]

    # Call the function
    result = task_func(X, Y)

    # Assertions to verify the output
    assert isinstance(result, list), "The result should be a list"
    assert len(result) == 2, "The result should contain two elements"
    assert all(isinstance(x, (int, float)) for x in result[0]), "The first element should be a list of floats or ints"
    assert isinstance(result[1], plt.Axes), "The second element should be a matplotlib Axes object"

    # Close the plot to avoid hanging the test
    plt.close()