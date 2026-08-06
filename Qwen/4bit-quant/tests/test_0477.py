import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0477 import task_func


def test_task_func():
    # Test with a simple quadratic function
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([2, 4, 6, 8, 10])  # Y = 2X, which is a linear function, but should work for task_func

    # Call the function
    params, ax = task_func(X, Y)

    # Check if the parameters are close to the expected values
    # Since it's a linear function, we expect a and c to be close to 0, and b to be close to 2
    assert len(params) == 3, "The number of parameters should be 3."
    assert np.isclose(params[0], 0, atol=1e-6), "Coefficient 'a' should be close to 0."
    assert np.isclose(params[1], 2, atol=1e-6), "Coefficient 'b' should be close to 2."
    assert np.isclose(params[2], 0, atol=1e-6), "Coefficient 'c' should be close to 0."

    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes), "The returned object should be an instance of matplotlib.axes._subplots.AxesSubplot."

    # Close the plot to avoid displaying it during tests
    plt.close(fig)

# Run the tests
if __name__ == "__main__":
    pytest.main()