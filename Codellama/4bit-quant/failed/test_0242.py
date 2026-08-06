import pytest
from src_0242 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def test_task_func():
    # Test case 1: Empty array
    original = []
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 0
    assert norm_arr.size == 0
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 2: Non-empty array
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 3: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 4: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 5: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 6: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 7: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 8: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 9: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"

    # Test case 10: Non-empty array with different values
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert arr.size == 3
    assert norm_arr.size == 3
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() == "Original"
    assert ax.get_legend() == "Normalized"