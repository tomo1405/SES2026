import pytest
from src_0911 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_valid_input():
    letters = ['A', 'B', 'C']
    repetitions = [3, 5, 2]
    colors = ['red', 'blue', 'green']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the bar chart is created correctly
    assert isinstance(ax, plt.AxesSubplot)
    assert len(ax.patches) == len(letters)
    
    # Check if the data is plotted correctly
    for i, bar in enumerate(ax.patches):
        assert bar.get_height() == repetitions[i]
        assert bar.get_color() == colors[i]

def test_task_func_invalid_length():
    with pytest.raises(ValueError, match="All lists must be the same length and non-empty."):
        task_func(['A', 'B'], [3, 5, 2], ['red', 'blue'])

def test_task_func_empty_input():
    with pytest.raises(ValueError, match="All lists must be the same length and non-empty."):
        task_func([], [], [])

def test_task_func_single_element():
    letters = ['X']
    repetitions = [10]
    colors = ['purple']
    
    ax = task_func(letters, repetitions, colors)
    
    assert isinstance(ax, plt.AxesSubplot)
    assert len(ax.patches) == len(letters)
    for i, bar in enumerate(ax.patches):
        assert bar.get_height() == repetitions[i]
        assert bar.get_color() == colors[i]

def test_task_func_large_input():
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    repetitions = np.random.randint(1, 100, size=len(letters))
    colors = ['black'] * len(letters)
    
    ax = task_func(letters, repetitions, colors)
    
    assert isinstance(ax, plt.AxesSubplot)
    assert len(ax.patches) == len(letters)
    for i, bar in enumerate(ax.patches):
        assert bar.get_height() == repetitions[i]
        assert bar.get_color() == colors[i]

def test_task_func_plot_capture():
    letters = ['A', 'B', 'C']
    repetitions = [3, 5, 2]
    colors = ['red', 'blue', 'green']
    
    fig, ax = plt.subplots()
    ax = task_func(letters, repetitions, colors, ax=ax)
    
    # Capture the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the image to base64 to check if it's valid
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert len(encoded_image) > 0