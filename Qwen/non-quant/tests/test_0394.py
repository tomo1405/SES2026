import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_output():
    # Capture the figure output
    fig = task_func(mu=0, sigma=1)
    
    # Convert the figure to a byte stream
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the byte stream to base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Check if the image is not empty
    assert len(image_base64) > 0

def test_task_func_randomness():
    # Set a specific seed
    np.random.seed(77)
    samples1 = np.random.normal(0, 1, 1000)
    
    # Call the function with the same seed
    fig = task_func(mu=0, sigma=1, seed=77)
    
    # Extract the data from the histogram
    ax = fig.axes[0]
    _, bins, _ = ax.hist([], bins=30, density=True, alpha=0.6, color='g')
    hist_data, _ = np.histogram(samples1, bins=bins, density=True)
    
    # Check if the histogram data matches
    assert np.allclose(ax.patches[0].get_height(), hist_data[0])

def test_task_func_subplots():
    fig = task_func(mu=0, sigma=1)
    
    # Check if there are two subplots
    assert len(fig.axes) == 2
    
    # Check if the first subplot is a histogram
    assert isinstance(fig.axes[0], plt.Axes)
    assert len(fig.axes[0].patches) > 0
    
    # Check if the second subplot is a probability plot
    assert isinstance(fig.axes[1], plt.Axes)
    assert len(fig.axes[1].lines) > 0