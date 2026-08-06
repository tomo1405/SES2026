import pytest
from src_0625 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    # Arrange
    L = [[1, 2], [3, 4], [5, 6]]
    expected_shape = (3, 2)

    # Act
    pca_result, ax = task_func(L)

    # Assert
    assert pca_result.shape == expected_shape, "The shape of the PCA result is incorrect."
    assert isinstance(ax, plt.Axes), "The returned object is not a matplotlib Axes instance."

def test_task_func_with_empty_data():
    # Arrange
    L = []

    # Act & Assert
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_single_point():
    # Arrange
    L = [[1, 2]]

    # Act
    pca_result, ax = task_func(L)

    # Assert
    assert pca_result.shape == (1, 2), "The shape of the PCA result is incorrect."
    assert isinstance(ax, plt.Axes), "The returned object is not a matplotlib Axes instance."

def test_task_func_with_non_numeric_data():
    # Arrange
    L = [['a', 'b'], ['c', 'd']]

    # Act & Assert
    with pytest.raises(ValueError):
        task_func(L)