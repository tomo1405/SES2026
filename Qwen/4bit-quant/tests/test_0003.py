import statistics

from src_0003 import task_func


def test_task_func():
    # Test with a small set of letters
    letters = ['A', 'B', 'C']
    result = task_func(letters)
    
    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check if all keys from the input are present in the result
    assert set(result.keys()) == set(letters)
    
    # Check if each value is a list of integers
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(x, int) for x in values)
    
    # Check if the dictionary is sorted by the mean of the lists in descending order
    means = [statistics.mean(values) for values in result.values()]
    assert means == sorted(means, reverse=True)

def test_task_func_with_single_letter():
    # Test with a single letter
    letters = ['X']
    result = task_func(letters)
    
    # Check if the result is a dictionary with one key-value pair
    assert len(result) == 1
    assert list(result.keys())[0] == 'X'
    assert isinstance(result['X'], list)
    assert all(isinstance(x, int) for x in result['X'])

def test_task_func_with_empty_list():
    # Test with an empty list of letters
    letters = []
    result = task_func(letters)
    
    # Check if the result is an empty dictionary
    assert result == {}

def test_task_func_with_repeated_letters():
    # Test with repeated letters
    letters = ['A', 'A', 'B', 'B', 'C']
    result = task_func(letters)
    
    # Check if the result is a dictionary with unique keys
    assert set(result.keys()) == {'A', 'B', 'C'}
    assert len(result) == 3
    
    # Check if each value is a list of integers
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(x, int) for x in values)
    
    # Check if the dictionary is sorted by the mean of the lists in descending order
    means = [statistics.mean(values) for values in result.values()]
    assert means == sorted(means, reverse=True)