python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytest

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

def test_task_func():
    # Test case 1: Test that the function returns a dictionary with the updated key-value pair
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    expected_dictionary = {'a': 1, 'b': 2}
    expected_data = pd.Series(np.random.normal(loc=2, scale=2, size=100))
    expected_ax = plt.hist(expected_data, bins=30, density=True)
    result_dictionary, result_data, result_ax = task_func(dictionary, key, value)
    assert result_dictionary == expected_dictionary
    assert result_data.equals(expected_data)
    assert result_ax == expected_ax
    
    # Test case 2: Test that the function raises a ValueError when the value is not a number
    dictionary = {'a': 1}
    key = 'b'
    value = 'c'
    with pytest.raises(ValueError):
        task_func(dictionary, key, value)
    
    # Test case 3: Test that the function returns the expected number of data points
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    n = 50
    expected_data = pd.Series(np.random.normal(loc=2, scale=2, size=50))
    result_data = task_func(dictionary, key, value, n=n)[1]
    assert len(result_data) == n
    
    # Test case 4: Test that the function returns the expected number of bins
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    bins = 5
    expected_ax = plt.hist(expected_data, bins=5, density=True)
    result_ax = task_func(dictionary, key, value, bins=bins)[2]
    assert result_ax == expected_ax
    
    # Test case 5: Test that the function returns the expected seed value
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    seed = 123
    np.random.seed(seed)
    expected_data = pd.Series(np.random.normal(loc=2, scale=2, size=100))
    result_data = task_func(dictionary, key, value, seed=seed)[1]
    assert result_data.equals(expected_data)