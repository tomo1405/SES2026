import pytest
from src_0625 import task_func

def test_task_func():
    L = [[1, 2], [3, 4], [5, 6]]
    pca_result, ax = task_func(L)
    assert pca_result.shape == (3, 2)
    assert ax.get_xlabel() == 'component 1'
    assert ax.get_ylabel() == 'component 2'

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func([[1, 2], [3, 4], [5, 6, 7]])