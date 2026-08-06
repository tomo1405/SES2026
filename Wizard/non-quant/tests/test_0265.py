python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    np.random.seed(seed)
    # Test that value is a number
    try:
        float(value)
    except ValueError:
        raise ValueError("Value must be a number.")
    # Update the dictionary
    dictionary[key] = value
    
    # Generate the dataset
    data = np.random.normal(loc=float(value), scale=float(value), size=n)
    
    # Plot the histogram of the generated data and get the axes object
    _, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True)
    data = pd.Series(data)
    return dictionary, data, ax

# Test case 1: Test that the function returns a dictionary with the updated key-value pair
def test_task_func_1():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    result = task_func(dictionary, key, value)
    assert result[0] == {'a': 1, 'b': 2}

# Test case 2: Test that the function returns a pandas Series object with the generated data
def test_task_func_2():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    result = task_func(dictionary, key, value)
    assert isinstance(result[1], pd.Series)

# Test case 3: Test that the function returns a matplotlib Axes object with the histogram plot
def test_task_func_3():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    result = task_func(dictionary, key, value)
    assert isinstance(result[2], plt.Axes)

# Test case 4: Test that the function raises a ValueError if the value is not a number
def test_task_func_4():
    dictionary = {'a': 1}
    key = 'b'
    value = 'c'
    try:
        task_func(dictionary, key, value)
    except ValueError as e:
        assert str(e) == "Value must be a number."