import pytest
from src_0417 import task_func

def test_task_func():
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
        {"a": 7, "b": 8, "c": 9}
    ]

    # Test with default column
    result = task_func(data)
    assert result is not None
    assert isinstance(result, sns.heatmap)

    # Test with specified column
    result = task_func(data, column="a")
    assert result is not None
    assert isinstance(result, sns.heatmap)

    # Test with invalid column
    result = task_func(data, column="d")
    assert result is None

    # Test with empty data
    result = task_func([])
    assert result is None