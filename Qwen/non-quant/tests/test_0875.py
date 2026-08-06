import pytest
from src_0875 import task_func
from scipy.spatial import distance

def test_task_func():
    # Test with no points
    assert task_func([]) == []

    # Test with one point
    assert task_func([(0, 0)]) == []

    # Test with two points
    assert task_func([(0, 0), (3, 4)]) == [5.0]

    # Test with three points
    assert task_func([(0, 0), (3, 4), (6, 8)]) == [5.0, 5.0]

    # Test with four points
    assert task_func([(0, 0), (3, 4), (6, 8), (9, 12)]) == [5.0, 5.0, 5.0]

    # Test with points in different dimensions
    assert task_func([(0, 0, 0), (3, 4, 0)]) == [5.0]

    # Test with negative coordinates
    assert task_func([(-3, -4), (0, 0)]) == [5.0]

    # Test with floating point coordinates
    assert pytest.approx(task_func([(0.0, 0.0), (3.0, 4.0)]), abs=1e-6) == [5.0]

    # Test with non-numeric coordinates
    with pytest.raises(ValueError):
        task_func([(0, 'a'), (3, 4)])

    # Test with non-list input
    with pytest.raises(TypeError):
        task_func("not a list")

    # Test with non-tuple point input
    with pytest.raises(ValueError):
        task_func([[0, 0], (3, 4)])