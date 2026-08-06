python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data, column):
    df = pd.DataFrame(data)
    # Define the categories
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Count occurrences of each category
    counts = df[column].value_counts()
    missing_categories = list(set(CATEGORIES) - set(counts.index))
    for category in missing_categories:
        counts[category] = 0

    counts = counts.reindex(CATEGORIES)
    
    # Plotting
    ax = counts.plot(kind='bar')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    plt.show()
    
    return ax

def test_task_func():
    # Test case 1
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]}
    column = 'A'
    expected_ax = task_func(data, column)
    assert isinstance(expected_ax, type(plt.subplots()[0]))
    
    # Test case 2
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]}
    column = 'B'
    expected_ax = task_func(data, column)
    assert isinstance(expected_ax, type(plt.subplots()[0]))
    
    # Test case 3
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]}
    column = 'C'
    expected_ax = task_func(data, column)
    assert isinstance(expected_ax, type(plt.subplots()[0]))
    
    # Test case 4
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]}
    column = 'D'
    expected_ax = task_func(data, column)
    assert isinstance(expected_ax, type(plt.subplots()[0]))
    
    # Test case 5
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]}
    column = 'E'
    expected_ax = task_func(data, column)
    assert isinstance(expected_ax, type(plt.subplots()[0]))