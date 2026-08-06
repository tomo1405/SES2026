import pytest
from src_0004 import task_func
import numpy as np

@pytest.fixture
def letters():
    return ['A', 'B', 'C']

def test_task_func_returns_dict(letters):
    result = task_func(letters)
    assert isinstance(result, dict)

def test_task_func_keys_match_input(letters):
    result = task_func(letters)
    assert set(result.keys()) == set(letters)

def test_task_func_values_are_floats(letters):
    result = task_func(letters)
    for value in result.values():
        assert isinstance(value, float)

def test_task_func_means_correct(letters):
    # Mocking the random number generation to control the output
    mock_random_numbers = {
        'A': [10, 20, 30],
        'B': [40, 50, 60],
        'C': [70, 80, 90]
    }
    with patch('src_0004.random.randint', side_effect=lambda a, b: mock_random_numbers[letters.pop()][0]):
        result = task_func(letters)
        assert result['A'] == np.mean(mock_random_numbers['A'])
        assert result['B'] == np.mean(mock_random_numbers['B'])
        assert result['C'] == np.mean(mock_random_numbers['C'])

def test_task_func_length_of_values(letters):
    result = task_func(letters)
    for key, value in result.items():
        assert len(result[key]) == 1  # Mean should be a single value

def test_task_func_with_empty_input():
    result = task_func([])
    assert result == {}

def test_task_func_with_single_letter():
    result = task_func(['X'])
    assert len(result) == 1
    assert isinstance(result['X'], float)