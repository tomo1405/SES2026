import pytest
from src_0621 import task_func

def test_task_func():
    L = [(2, 3), (4, 5)]
    expected_shape = (L[0][0] * L[0][1], L[1][0] * L[1][1])
    df = task_func(L)
    actual_shape = df.shape
    assert actual_shape == expected_shape, "The shape of the DataFrame returned by task_func is incorrect."

def test_task_func_invalid_input():
    L = "invalid input"
    with pytest.raises(ValueError):
        task_func(L)