from collections import Counter

from src_0862 import task_func


def test_task_func():
    # Test with an empty list of lists
    assert task_func([]) == []

    # Test with a single empty list
    assert task_func([[]]) == [Counter()]

    # Test with a single list containing one element
    result = task_func([[1]])
    assert len(result) == 1
    assert isinstance(result[0], Counter)
    assert all(item in POSSIBLE_ITEMS for item in result[0].keys())

    # Test with a single list containing multiple elements
    result = task_func([[1, 2, 3]])
    assert len(result) == 1
    assert isinstance(result[0], Counter)
    assert sum(result[0].values()) == 3
    assert all(item in POSSIBLE_ITEMS for item in result[0].keys())

    # Test with multiple lists
    result = task_func([[1, 2], [3, 4, 5]])
    assert len(result) == 2
    for basket in result:
        assert isinstance(basket, Counter)
        assert all(item in POSSIBLE_ITEMS for item in basket.keys())

    # Test with fixed seed to ensure reproducibility
    seed(42)
    expected_result = task_func([[1, 2], [3, 4, 5]])
    seed(42)
    actual_result = task_func([[1, 2], [3, 4, 5]])
    assert expected_result == actual_result