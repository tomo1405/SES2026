import pytest
from src_0370 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Test with a simple list of numbers
    data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
    ax = task_func(data)
    
    # Check if the axis object is returned
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram is plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 2  # One for the histogram and one for the fitted line
    
    # Check if the title contains the correct mu and std values
    mu, std = stats.norm.fit(data)
    expected_title = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
    assert ax.get_title() == expected_title

    # Check if the plot can be saved to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert img_base64.startswith('iVBORw0KGgoAAAANSUhEUgAAAAUA')

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])