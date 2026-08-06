import pytest
from src_0370 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_output():
    # Create a sample list of data
    data = [1, 2, 2.5, 400, 6, 0]
    
    # Call the function
    ax = task_func(data)
    
    # Check if the axis object is returned
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Check if the histogram is plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1, "There should be one line in the plot (the histogram)"
    
    # Check if the normal distribution fit line is plotted
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 2, "There should be two lines in the plot (the histogram and the fit line)"
    
    # Check if the title contains the correct mu and std values
    mu, std = stats.norm.fit(data)
    expected_title = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
    assert ax.get_title() == expected_title, "The title does not match the expected format"

def test_task_func_plot_content():
    # Create a sample list of data
    data = [1, 2, 2.5, 400, 6, 0]
    
    # Call the function
    ax = task_func(data)
    
    # Save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the image to base64 to check its content
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Check if the image is not empty
    assert image_base64, "The plot image should not be empty"