python
import pytest
from src_0052 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    age = 25
    height = 180
    expected_output = (
        {"Age": [25, 30, 35], "Height": [170, 180, 190], "Cluster": [0, 1, 2]},
        None,
    )
    assert task_func(df, age, height) == expected_output

    # Test case 2: Invalid input (age is negative)
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    age = -25
    height = 180
    expected_output = (
        {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200], "Cluster": [0, 0, 0, 0, 0]},
        None,
    )
    assert task_func(df, age, height) == expected_output

    # Test case 3: Invalid input (height is negative)
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    age = 25
    height = -180
    expected_output = (
        {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200], "Cluster": [0, 0, 0, 0, 0]},
        None,
    )
    assert task_func(df, age, height) == expected_output

    # Test case 4: Invalid input (no rows in filtered DataFrame)
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    age = 50
    height = 250
    expected_output = (
        {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200], "Cluster": [0, 0, 0, 0, 0]},
        None,
    )
    assert task_func(df, age, height) == expected_output

    # Test case 5: Invalid input (less than 3 rows in filtered DataFrame)
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    age = 25
    height = 180
    expected_output = (
        {"Age": [25, 30, 35], "Height": [170, 180, 190], "Cluster": [0, 1, 2]},
        None,
    )
    assert task_func(df, age, height) == expected_output