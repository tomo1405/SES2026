python
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

def task_func(dictionary, new_key, new_value):
    # Add new key-value pair to the dictionary
    dictionary[new_key] = new_value
    
    # Plot the distribution of its values
    values_counts = collections.Counter(dictionary.values())
    ax = sns.barplot(y=list(values_counts.keys()), x=list(values_counts.values()))
    plt.title("Distribution of Dictionary Values")
    plt.xlabel("Values")
    plt.ylabel("Counts")
    
    return dictionary, ax

def test_task_func():
    # Test case 1: Valid input
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    new_key = 'd'
    new_value = 4
    expected_output = ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, None)
    assert task_func(dictionary, new_key, new_value) == expected_output
    
    # Test case 2: Invalid input (new_key is not a string)
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    new_key = 123
    new_value = 4
    with pytest.raises(TypeError):
        task_func(dictionary, new_key, new_value)
    
    # Test case 3: Invalid input (new_value is not an integer)
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    new_key = 'd'
    new_value = 'abc'
    with pytest.raises(TypeError):
        task_func(dictionary, new_key, new_value)