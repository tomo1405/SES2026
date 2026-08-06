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
    # Test case 1: valid input
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    ax = task_func(letters, repetitions, colors)
    assert ax is not None
    
    # Test case 2: invalid input (empty list)
    letters = []
    repetitions = []
    colors = []
    with pytest.raises(ValueError):
        ax = task_func(letters, repetitions, colors)
        
    # Test case 3: invalid input (unequal length lists)
    letters = ['a', 'b', 'c']
    repetitions = [1, 2]
    colors = ['red', 'green', 'blue']
    with pytest.raises(ValueError):
        ax = task_func(letters, repetitions, colors)
        
    # Test case 4: invalid input (non-numeric repetitions)
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, '3']
    colors = ['red', 'green', 'blue']
    with pytest.raises(ValueError):
        ax = task_func(letters, repetitions, colors)