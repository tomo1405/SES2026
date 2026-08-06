python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytest

def task_func(elements, seed=0):
    np.random.seed(seed)
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("Element must be a positive integer.")
        
    steps = np.random.choice([-1, 1], size=elements)
    walk = np.cumsum(steps)
    descriptive_stats = pd.Series(walk).describe(percentiles=[.05, .25, .5, .75, .95]).to_dict()
    
    plt.figure(figsize=(10, 6))
    plt.plot(walk)
    plt.title('Random Walk')
    return descriptive_stats, plt.gca()

def test_task_func():
    # Test case 1: Valid input
    assert task_func(10, seed=42)[0]['50%'] == 4.5
    
    # Test case 2: Invalid input (not a positive integer)
    with pytest.raises(ValueError):
        task_func(-10, seed=42)
    
    # Test case 3: Invalid input (not an integer)
    with pytest.raises(ValueError):
        task_func(10.5, seed=42)
    
    # Test case 4: Invalid input (seed is not an integer)
    with pytest.raises(ValueError):
        task_func(10, seed='42')