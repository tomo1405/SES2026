import pytest
from src_0281 import task_func

@pytest.mark.parametrize("signal, precision, seed, expected_output", [
    (np.array([1, 2, 3, 4, 5]), 2, 777, (np.array([15., -3.5+0.866j, 0.+0.j, -3.5-0.866j]), [None, None])),
    (np.array([5, 4, 3, 2, 1]), 3, 777, (np.array([15., -3.5+0.866j, 0.+0.j, -3.5-0.866j]), [None, None])),
    (np.array([1, 2, 3, 4, 5]), 1, 777, (np.array([15., -4.+0.j, 0.+0.j, -4.+0.j]), [None, None])),
])
def test_task_func(signal, precision, seed, expected_output):
    np.random.seed(seed)
    result = task_func(signal, precision, seed)
    assert result == expected_output