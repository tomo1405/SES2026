import pytest
from src_0006 import task_func

def test_task_func():
    # Test that the function returns a dictionary
    result = task_func()
    assert isinstance(result, dict)

    # Test that the dictionary keys are lowercase letters
    assert all(isinstance(key, str) and key.islower() for key in result.keys())

    # Test that each value is a list of integers
    for values in result.values():
        assert isinstance(values, list)
        assert all(isinstance(value, int) for value in values)

    # Test that the standard deviation calculation is correct
    for key, values in result.items():
        mean = sum(values) / len(values)
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
        assert math.isclose(result[key], std_dev)

    # Test with a custom set of letters
    custom_letters = ['a', 'b', 'c']
    custom_result = task_func(custom_letters)
    assert set(custom_result.keys()) == set(custom_letters)

    # Test with an empty list of letters
    empty_result = task_func([])
    assert empty_result == {}

    # Test with a single letter
    single_letter_result = task_func(['x'])
    assert list(single_letter_result.keys()) == ['x']
    assert isinstance(single_letter_result['x'], list)
    assert len(single_letter_result['x']) > 0