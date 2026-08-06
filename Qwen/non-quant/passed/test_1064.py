import pytest
from src_1064 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax = task_func(arr)

    # Check if the plot has the correct title
    assert ax.get_title() == "Explained Variance Ratio of Principal Components"

    # Check if the x-ticks and labels are set correctly
    x_ticks = ax.get_xticks()
    x_tick_labels = [item.get_text() for item in ax.get_xticklabels()]
    assert np.array_equal(x_ticks, [0])
    assert x_tick_labels == ["PC1"]

    # Check if the bar plot has the correct data
    bars = ax.patches
    assert len(bars) == 1
    assert np.isclose(bars[0].get_height(), 1.0)

    # Save the plot to a buffer and check its content
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # Assert that the image is not empty
    assert len(image_base64) > 0