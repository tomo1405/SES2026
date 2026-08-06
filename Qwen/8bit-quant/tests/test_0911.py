import pytest
from src_0911 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    letters = ['a', 'b', 'c']
    repetitions = [3, 2, 1]
    colors = ['red', 'green', 'blue']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the bar chart has the correct number of bars
    assert len(ax.patches) == 3
    
    # Check if the heights of the bars match the repetitions
    for i, patch in enumerate(ax.patches):
        assert patch.get_height() == repetitions[i]
    
    # Check if the x-ticks match the letters
    assert all(label.get_text() == letter for label, letter in zip(ax.get_xticklabels(), letters))
    
    # Check if the colors of the bars match the specified colors
    for i, patch in enumerate(ax.patches):
        assert patch.get_facecolor() == plt.colors.to_rgba(colors[i])

def test_task_func_empty_lists():
    with pytest.raises(ValueError):
        task_func([], [], [])

def test_task_func_different_lengths():
    with pytest.raises(ValueError):
        task_func(['a', 'b'], [3, 2], ['red'])

def test_task_func_single_element():
    letters = ['a']
    repetitions = [5]
    colors = ['red']
    
    ax = task_func(letters, repetitions, colors)
    
    # Check if the bar chart has the correct number of bars
    assert len(ax.patches) == 1
    
    # Check if the height of the bar matches the repetition
    assert ax.patches[0].get_height() == repetitions[0]
    
    # Check if the x-tick matches the letter
    assert ax.get_xticklabels()[0].get_text() == letters[0]
    
    # Check if the color of the bar matches the specified color
    assert ax.patches[0].get_facecolor() == plt.colors.to_rgba(colors[0])