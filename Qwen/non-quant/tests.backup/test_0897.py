import pytest
from src_0897 import task_func
from collections import Counter

def test_task_func():
    # Test with default parameters
    result = task_func(5, 10)
    assert isinstance(result, Counter)
    assert sum(result.values()) == 50  # 10 strings of length 5 each

    # Test with specific seed to ensure reproducibility
    result_with_seed = task_func(3, 4, seed=42)
    expected_result = Counter({'a': 6, 'b': 5, 'c': 5, 'd': 5, 'e': 3})
    assert result_with_seed == expected_result

    # Test with different length and count
    result_large = task_func(10, 5)
    assert isinstance(result_large, Counter)
    assert sum(result_large.values()) == 50  # 5 strings of length 10 each

    # Test with zero count
    result_zero_count = task_func(5, 0)
    assert result_zero_count == Counter()

    # Test with zero length
    result_zero_length = task_func(0, 5)
    assert result_zero_length == Counter()

    # Test with large seed value
    result_large_seed = task_func(5, 10, seed=999999999)
    assert isinstance(result_large_seed, Counter)
    assert sum(result_large_seed.values()) == 50  # 10 strings of length 5 each