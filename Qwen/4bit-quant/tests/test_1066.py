from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_1066 import task_func


def test_task_func():
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax = task_func(arr)

    # Check if the plot has been created
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."

    # Check if the plot title is set correctly
    assert ax.get_title() == "Absolute values of FFT coefficients", "The plot title is incorrect."

    # Capture the plot to check its content
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue(), "The plot should not be empty."

    # Clean up the plot
    plt.close()

# Run the test
if __name__ == "__main__":
    pytest.main()