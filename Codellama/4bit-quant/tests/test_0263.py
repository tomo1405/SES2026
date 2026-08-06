import collections

from src_0263 import task_func


def test_task_func():
    # Test case 1: add new key-value pair to the dictionary
    dictionary = {"a": 1, "b": 2, "c": 3}
    new_key = "d"
    new_value = 4
    expected_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
    actual_dictionary, ax = task_func(dictionary, new_key, new_value)
    assert actual_dictionary == expected_dictionary
    
    # Test case 2: plot the distribution of its values
    values_counts = collections.Counter(dictionary.values())
    expected_values_counts = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert values_counts == expected_values_counts
    ax = sns.barplot(y=list(values_counts.keys()), x=list(values_counts.values()))
    plt.title("Distribution of Dictionary Values")
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.show()