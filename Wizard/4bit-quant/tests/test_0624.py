python
import pytest
from src_0624 import task_func

def test_task_func():
    # Test case 1
    L = [[1, 2, 3], [4, 5, 6]]
    ax = task_func(L)
    assert ax.get_xlabel() == '0'
    assert ax.get_ylabel() == '0'
    assert ax.get_title() == 'K-means clustering'
    assert len(ax.collections) == 3
    assert ax.collections[0].get_offsets().shape == (3, 1)
    assert ax.collections[1].get_offsets().shape == (3, 1)
    assert ax.collections[2].get_offsets().shape == (3, 1)
    assert ax.collections[0].get_color() == (0.0, 0.0, 0.0, 1.0)
    assert ax.collections[1].get_color() == (0.5, 0.5, 0.5, 1.0)
    assert ax.collections[2].get_color() == (1.0, 1.0, 1.0, 1.0)

    # Test case 2
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert ax.get_xlabel() == '0'
    assert ax.get_ylabel() == '0'
    assert ax.get_title() == 'K-means clustering'
    assert len(ax.collections) == 3
    assert ax.collections[0].get_offsets().shape == (3, 1)
    assert ax.collections[1].get_offsets().shape == (3, 1)
    assert ax.collections[2].get_offsets().shape == (3, 1)
    assert ax.collections[0].get_color() == (0.0, 0.0, 0.0, 1.0)
    assert ax.collections[1].get_color() == (0.5, 0.5, 0.5, 1.0)
    assert ax.collections[2].get_color() == (1.0, 1.0, 1.0, 1.0)

    # Test case 3
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    ax = task_func(L)
    assert ax.get_xlabel() == '0'
    assert ax.get_ylabel() == '0'
    assert ax.get_title() == 'K-means clustering'
    assert len(ax.collections) == 3
    assert ax.collections[0].get_offsets().shape == (4, 1)
    assert ax.collections[1].get_offsets().shape == (4, 1)
    assert ax.collections[2].get_offsets().shape == (4, 1)
    assert ax.collections[0].get_color() == (0.0, 0.0, 0.0, 1.0)
    assert ax.collections[1].get_color() == (0.5, 0.5, 0.5, 1.0)
    assert ax.collections[2].get_color() == (1.0, 1.0, 1.0, 1.0)