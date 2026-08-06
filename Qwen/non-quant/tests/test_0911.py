import pytest
from src_0911 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_valid_input():
    letters = ['A', 'B', 'C']
    repetitions = [3, 2, 1]
    colors = ['red', 'green', 'blue']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the axis object is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the bars are plotted correctly
    containers = ax.containers[0]
    heights = [bar.get_height() for bar in containers]
    assert heights == repetitions
    
    # Check if the colors are set correctly
    for bar, color in zip(containers, colors):
        assert bar.get_facecolor()[0] == plt.colors.to_rgb(color)[0]

def test_task_func_empty_lists():
    with pytest.raises(ValueError):
        task_func([], [], [])

def test_task_func_different_lengths():
    with pytest.raises(ValueError):
        task_func(['A', 'B'], [3], ['red', 'green'])

def test_task_func_single_element():
    letters = ['X']
    repetitions = [5]
    colors = ['purple']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the axis object is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the bars are plotted correctly
    containers = ax.containers[0]
    heights = [bar.get_height() for bar in containers]
    assert heights == repetitions
    
    # Check if the colors are set correctly
    for bar, color in zip(containers, colors):
        assert bar.get_facecolor()[0] == plt.colors.to_rgb(color)[0]

def test_task_func_with_zero_repetitions():
    letters = ['A', 'B', 'C']
    repetitions = [0, 2, 0]
    colors = ['red', 'green', 'blue']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the axis object is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the bars are plotted correctly
    containers = ax.containers[0]
    heights = [bar.get_height() for bar in containers]
    assert heights == repetitions
    
    # Check if the colors are set correctly
    for bar, color in zip(containers, colors):
        assert bar.get_facecolor()[0] == plt.colors.to_rgb(color)[0]

def test_task_func_plot_saving():
    letters = ['A', 'B', 'C']
    repetitions = [3, 2, 1]
    colors = ['red', 'green', 'blue']
    
    ax = task_func(letters, repetitions, colors)
    
    # Save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the buffer to base64 to check if it's a valid image
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert img_base64.startswith('iVBORw0KGgoAAAANSUhEUgAA')

# Run the tests
if __name__ == "__main__":
    pytest.main()