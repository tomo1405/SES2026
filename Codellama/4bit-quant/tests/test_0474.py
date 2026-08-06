import pytest
from src_0474 import task_func

def test_task_func():
    # Test that the function raises an error when n_walks or n_steps is negative
    with pytest.raises(ValueError):
        task_func(-1, 10)
    with pytest.raises(ValueError):
        task_func(10, -1)

    # Test that the function returns the correct number of walks
    n_walks = 10
    n_steps = 10
    walks = task_func(n_walks, n_steps)
    assert len(walks) == n_walks

    # Test that the function returns the correct number of steps in each walk
    for walk in walks:
        assert len(walk) == n_steps

    # Test that the function returns the correct type of data
    assert isinstance(walks, list)
    assert all(isinstance(walk, np.ndarray) for walk in walks)

    # Test that the function returns the correct values
    expected_walks = [np.array([-1, 1, 0, -1, 1, 0, -1, 1, 0, -1])]
    assert np.array_equal(walks, expected_walks)