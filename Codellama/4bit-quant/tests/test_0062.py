import pytest
from src_0062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def test_task_func():
    # Test with a list of integers
    result = [{'from_user': 1}, {'from_user': 4}, {'from_user': 9}]
    expected_square_roots = [1.0, 2.0, 3.0]
    expected_ax = plt.gca()
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

    # Test with a list of floats
    result = [{'from_user': 1.5}, {'from_user': 4.5}, {'from_user': 9.5}]
    expected_square_roots = [1.22474487, 2.23606797, 3.25245991]
    expected_ax = plt.gca()
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

    # Test with a list of mixed types
    result = [{'from_user': 1}, {'from_user': 4.5}, {'from_user': '9'}]
    expected_square_roots = [1.0, 2.23606797, 3.0]
    expected_ax = plt.gca()
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

    # Test with an empty list
    result = []
    expected_square_roots = []
    expected_ax = plt.gca()
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax