import pytest
from src_1066 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Create a sample array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax = task_func(arr)

    # Check if the plot has the correct title
    assert ax.get_title() == "Absolute values of FFT coefficients"

    # Check if the plot has the correct number of data points
    xdata, ydata = ax.lines[0].get_data()
    assert len(xdata) == len(ydata) == 3

    # Save the plot to a buffer and encode it in base64
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded_plot = base64.b64encode(buf.read()).decode('utf-8')

    # Optionally, you can save this encoded plot to a file or compare it with a reference plot
    # For now, we just print it
    print(encoded_plot)

    # Close the plot to free up memory
    plt.close(ax.figure)