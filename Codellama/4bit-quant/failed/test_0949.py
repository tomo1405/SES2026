import pytest
from src_0949 import task_func

def test_task_func():
    rows = 3
    columns = 2
    seed = 42
    expected_output = np.array([[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]])

    output = task_func(rows, columns, seed)

    assert np.allclose(output, expected_output)