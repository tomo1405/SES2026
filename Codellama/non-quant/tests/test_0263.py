import pytest
from src_0263 import task_func

def test_task_func():
    # Test case 1: Add new key-value pair to the dictionary
    dictionary = {"a": 1, "b": 2, "c": 3}
    new_key = "d"
    new_value = 4
    expected_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert task_func(dictionary, new_key, new_value) == expected_dictionary

    # Test case 2: Plot the distribution of its values
    dictionary = {"a": 1, "b": 2, "c": 3}
    new_key = "d"
    new_value = 4
    expected_ax = plt.bar(y=list(collections.Counter(dictionary.values()).keys()), x=list(collections.Counter(dictionary.values()).values()))
    plt.title("Distribution of Dictionary Values")
    plt.xlabel("Values")
    plt.ylabel("Counts")
    assert task_func(dictionary, new_key, new_value) == expected_ax