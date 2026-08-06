python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

# Test 1
def test_task_func_valid_input():
    assert task_func(10, seed=0) == ({'count': 10.0, 'mean': 0.0, 'std': 0.816496580927726, 'min': -4.0, '25%': -1.0, '50%': 0.0, '75%': 1.0, 'max': 4.0, '5%': -2.8284271247461903}, <matplotlib.axes._subplots.AxesSubplot object at 0x7f9d5d5d5a90>)

# Test 2
def test_task_func_invalid_input():
    try:
        task_func(-10, seed=0)
    except ValueError as e:
        assert str(e) == "Element must be a positive integer."
    else:
        assert False, "Expected ValueError"

# Test 3
def test_task_func_random_seed():
    assert task_func(10, seed=1) != task_func(10, seed=2)