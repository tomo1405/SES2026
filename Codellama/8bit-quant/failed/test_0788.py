import pytest
from src_0788 import task_func

def test_task_func():
    # Test case 1: same length arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    expected = 3
    assert task_func(array1, array2) == expected

    # Test case 2: different length arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(array1, array2)

    # Test case 3: empty arrays
    array1 = np.array([])
    array2 = np.array([])
    expected = 0
    assert task_func(array1, array2) == expected

    # Test case 4: arrays with different lengths
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6, 7])
    with pytest.raises(ValueError):
        task_func(array1, array2)

    # Test case 5: arrays with different shapes
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    with pytest.raises(ValueError):
        task_func(array1, array2)

    # Test case 6: arrays with different types
    array1 = np.array([1, 2, 3], dtype=np.int32)
    array2 = np.array([4, 5, 6], dtype=np.int64)
    with pytest.raises(ValueError):
        task_func(array1, array2)