python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(letters, repetitions, colors):
    if len(letters) != len(repetitions) or len(letters) != len(colors) or len(letters) == 0:
        raise ValueError("All lists must be the same length and non-empty.")
        
    # Count the frequency of each letter based on repetitions
    counts = np.array(repetitions)
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(letters, counts, color=colors)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    
    return ax

def test_task_func():
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    ax = task_func(letters, repetitions, colors)
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Frequency of Letters'
    assert ax.patches[0].get_facecolor() == (1.0, 0.0, 0.0, 1.0)
    assert ax.patches[1].get_facecolor() == (0.0, 1.0, 0.0, 1.0)
    assert ax.patches[2].get_facecolor() == (0.0, 0.0, 1.0, 1.0)
    assert ax.patches[0].get_height() == 1
    assert ax.patches[1].get_height() == 2
    assert ax.patches[2].get_height() == 3