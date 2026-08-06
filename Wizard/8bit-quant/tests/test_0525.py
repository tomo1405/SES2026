python
import pytest
from src_0525 import task_func

def test_task_func():
    # Test empty input
    with pytest.raises(ValueError):
        task_func([])

    # Test non-list input
    with pytest.raises(TypeError):
        task_func("not a list")

    # Test non-dict input
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

    # Test non-numeric input
    with pytest.raises(TypeError):
        task_func([{"a": "b"}, {"c": "d"}])

    # Test valid input
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
        {"a": 7, "b": 8, "c": 9},
    ]
    result, axes = task_func(data)
    assert isinstance(result, dict)
    assert all(isinstance(v, dict) for v in result.values())
    assert all(isinstance(v, dict) for v in result.values())
    assert all(isinstance(v, (int, float)) for d in result.values() for v in d.values())
    assert all(isinstance(ax, plt.Axes) for ax in axes)