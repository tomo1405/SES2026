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
def test_task_func_1():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, plt.Axes)
    assert len(descriptive_stats) == 5
    assert 'mean' in descriptive_stats
    assert 'std' in descriptive_stats
    assert '5%' in descriptive_stats
    assert '25%' in descriptive_stats
    assert '50%' in descriptive_stats
    assert '75%' in descriptive_stats
    assert '95%' in descriptive_stats
    assert ax.get_title() == 'Random Walk'
    assert ax.get_xlabel() == 'Step'
    assert ax.get_ylabel() == 'Value'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()) == 2
    
# Test 2
def test_task_func_2():
    elements = 10
    seed = 1
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, plt.Axes)
    assert len(descriptive_stats) == 5
    assert 'mean' in descriptive_stats
    assert 'std' in descriptive_stats
    assert '5%' in descriptive_stats
    assert '25%' in descriptive_stats
    assert '50%' in descriptive_stats
    assert '75%' in descriptive_stats
    assert '95%' in descriptive_stats
    assert ax.get_title() == 'Random Walk'
    assert ax.get_xlabel() == 'Step'
    assert ax.get_ylabel() == 'Value'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()) == 2
    
# Test 3
def test_task_func_3():
    elements = 0
    seed = 0
    try:
        descriptive_stats, ax = task_func(elements, seed)
    except ValueError as e:
        assert str(e) == "Element must be a positive integer."
    else:
        assert False, "Expected ValueError"

# Test 4
def test_task_func_4():
    elements = 10
    seed = 'a'
    try:
        descriptive_stats, ax = task_func(elements, seed)
    except ValueError as e:
        assert str(e) == "seed must be an integer."
    else:
        assert False, "Expected ValueError"

# Test 5
def test_task_func_5():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, plt.Axes)
    assert len(descriptive_stats) == 5
    assert 'mean' in descriptive_stats
    assert 'std' in descriptive_stats
    assert '5%' in descriptive_stats
    assert '25%' in descriptive_stats
    assert '50%' in descriptive_stats
    assert '75%' in descriptive_stats
    assert '95%' in descriptive_stats
    assert ax.get_title() == 'Random Walk'
    assert ax.get_xlabel() == 'Step'
    assert ax.get_ylabel() == 'Value'
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()) == 2