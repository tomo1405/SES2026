import pytest
from src_0278 import task_func
import math

def test_task_func_with_n_less_than_2():
    assert task_func(1) is None
    assert task_func(0) is None
    assert task_func(-1) is None

def test_task_func_with_n_equal_to_2():
    result = task_func(2)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_with_n_greater_than_2():
    result = task_func(5)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_distance_calculation():
    # Mocking random points for reproducibility
    def mock_random():
        return [0.1, 0.2, 0.3, 0.4, 0.5]

    with pytest.monkeypatch.context() as mp:
        mp.setattr(random, 'random', lambda: mock_random().pop(0))
        result = task_func(2)
        distance = math.hypot(result[0][0] - result[1][0], result[0][1] - result[1][1])
        assert distance == math.hypot(0.1 - 0.2, 0.1 - 0.3)