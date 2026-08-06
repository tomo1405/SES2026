import pytest
from src_0310 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    return [
        [1, 2, 3],
        [],
        [10, 20, 30, 40, 50]
    ]

def test_task_func_with_non_empty_lists(sample_data):
    result = task_func(sample_data)
    assert len(result) == 3
    assert all(isinstance(sublist, list) for sublist in result)
    assert all(len(sublist) == len(original) for sublist, original in zip(result, sample_data))

def test_task_func_with_empty_list(sample_data):
    # The second list in sample_data is empty, it should be replaced with 5 random integers
    result = task_func(sample_data)
    assert len(result[1]) == 5
    assert all(isinstance(x, float) for x in result[1])

def test_task_func_randomness(sample_data):
    np.random.seed(42)
    result1 = task_func(sample_data)
    np.random.seed(42)
    result2 = task_func(sample_data)
    assert result1 == result2

def test_task_func_min_max_values(sample_data):
    result = task_func(sample_data)
    for sublist in result:
        assert min(sublist) >= 0
        assert max(sublist) <= 1

def test_task_func_with_single_element_lists():
    sample_data = [[5], [10], [15]]
    result = task_func(sample_data)
    assert all(sublist == [0.0] for sublist in result)

def test_task_func_with_identical_elements():
    sample_data = [[5, 5, 5], [10, 10, 10], [15, 15, 15]]
    result = task_func(sample_data)
    assert all(sublist == [0.0, 0.0, 0.0] for sublist in result)