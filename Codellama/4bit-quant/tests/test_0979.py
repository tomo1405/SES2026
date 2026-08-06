import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func():
    # Test 1: Input is not a numpy array
    with pytest.raises(ValueError):
        task_func(array=None)

    # Test 2: Input is not a 2D numpy array
    with pytest.raises(ValueError):
        task_func(array=np.array([1, 2, 3]))

    # Test 3: Input is a 2D numpy array with size 0
    with pytest.raises(ValueError):
        task_func(array=np.array([]))

    # Test 4: Input is a 2D numpy array with shape (1, 0)
    with pytest.raises(ValueError):
        task_func(array=np.array([[]]))

    # Test 5: Input is a 2D numpy array with shape (2, 0)
    with pytest.raises(ValueError):
        task_func(array=np.array([[], []]))

    # Test 6: Input is a 2D numpy array with shape (2, 1)
    array = np.array([[1], [2]])
    expected_output = pd.DataFrame(data=[[1], [2]], columns=["PC1"])
    assert task_func(array).equals(expected_output)

    # Test 7: Input is a 2D numpy array with shape (2, 2)
    array = np.array([[1, 2], [3, 4]])
    expected_output = pd.DataFrame(data=[[1, 2], [3, 4]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 8: Input is a 2D numpy array with shape (2, 3)
    array = np.array([[1, 2, 3], [4, 5, 6]])
    expected_output = pd.DataFrame(data=[[1, 2], [4, 5]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 9: Input is a 2D numpy array with shape (2, 4)
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    expected_output = pd.DataFrame(data=[[1, 2], [5, 6]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 10: Input is a 2D numpy array with shape (2, 5)
    array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    expected_output = pd.DataFrame(data=[[1, 2], [6, 7]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 11: Input is a 2D numpy array with shape (2, 6)
    array = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
    expected_output = pd.DataFrame(data=[[1, 2], [7, 8]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 12: Input is a 2D numpy array with shape (2, 7)
    array = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
    expected_output = pd.DataFrame(data=[[1, 2], [8, 9]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 13: Input is a 2D numpy array with shape (2, 8)
    array = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]])
    expected_output = pd.DataFrame(data=[[1, 2], [9, 10]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 14: Input is a 2D numpy array with shape (2, 9)
    array = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]])
    expected_output = pd.DataFrame(data=[[1, 2], [10, 11]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)

    # Test 15: Input is a 2D numpy array with shape (2, 10)
    array = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])
    expected_output = pd.DataFrame(data=[[1, 2], [11, 12]], columns=["PC1", "PC2"])
    assert task_func(array).equals(expected_output)