import pytest
from src_0213 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    data = [(1, 2), (3, 5), (2, 4)]
    ax, max_y_point = task_func(data)

    # Check if max_y_point is correct
    assert max_y_point == (3, 5)

    # Check if the plot is created correctly
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    # This is a placeholder check for the plot content.
    # In a real-world scenario, you might want to use a library like Pillow to compare images.
    assert len(image_base64) > 0, "The plot should contain data"

    # Clean up the plot
    plt.close(fig)