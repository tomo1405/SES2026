import pytest
from src_0376 import task_func

def test_task_func():
    # Test case 1: Test with a 2D array
    l = [[1, 2], [3, 4], [5, 6]]
    ax = task_func(l)
    assert ax is not None
    assert ax.get_xlabel() == 'First Principal Component'
    assert ax.get_ylabel() == 'Second Principal Component'
    assert ax.get_title() == 'PCA Result'

    # Test case 2: Test with a 1D array
    l = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(l)