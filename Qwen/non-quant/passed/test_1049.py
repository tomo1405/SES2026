import pytest
from src_1049 import task_func
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Test with a known date
    date_str = "2023-10-15"
    ax = task_func(date_str)
    
    # Check if the title is set correctly
    assert ax.get_title() == f"Sine Wave for {date_str} (Frequency: 15)"
    
    # Check if the x and y data are correct
    x_data, y_data = ax.lines[0].get_data()
    expected_x_data = np.linspace(0, 2 * np.pi, 1000)
    expected_y_data = np.sin(15 * expected_x_data)
    np.testing.assert_array_almost_equal(x_data, expected_x_data)
    np.testing.assert_array_almost_equal(y_data, expected_y_data)
    
    # Check if the plot can be saved to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert len(image_base64) > 0