import statistics

from src_0003 import task_func


def test_task_func():
    # Test case 1: Test with an empty input
    result = task_func([])
    assert result == {}

    # Test case 2: Test with a list of letters
    result = task_func(['A', 'B', 'C'])
    assert isinstance(result, dict)
    assert len(result) == 3
    assert all(letter in result for letter in ['A', 'B', 'C'])

    # Test case 3: Test with a list of letters and check the values
    result = task_func(['X', 'Y', 'Z'])
    assert isinstance(result, dict)
    assert len(result) == 3
    assert all(letter in result for letter in ['X', 'Y', 'Z'])
    assert all(isinstance(value, list) for value in result.values())
    assert all(isinstance(item, int) for value in result.values() for item in value)

    # Test case 4: Test with a list of letters and check the keys are sorted by descending mean
    result = task_func(['Q', 'W', 'E', 'R', 'T', 'Y'])
    assert isinstance(result, dict)
    assert len(result) == 6
    assert all(letter in result for letter in ['Q', 'W', 'E', 'R', 'T', 'Y'])
    assert result == dict(sorted(result.items(), key=lambda item: statistics.mean(item[1]), reverse=True))