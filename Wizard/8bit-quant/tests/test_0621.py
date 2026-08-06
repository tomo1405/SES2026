python
import numpy as np
import pandas as pd
import pytest

# Constants
RANGE = (1, 100)

def task_func(L):
    rows, columns = L[0][0] * L[0][1], L[1][0] * L[1][1]
    random_array = np.random.randint(RANGE[0], RANGE[1], size=(rows, columns))
    df = pd.DataFrame(random_array)
    
    return df

# Test case 1
def test_task_func_1():
    L = [(2, 3), (4, 5)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(6, 10)))
    assert task_func(L).equals(expected_df)

# Test case 2
def test_task_func_2():
    L = [(1, 2), (3, 4)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(6, 8)))
    assert task_func(L).equals(expected_df)

# Test case 3
def test_task_func_3():
    L = [(5, 7), (8, 10)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(40, 40)))
    assert task_func(L).equals(expected_df)

# Test case 4
def test_task_func_4():
    L = [(10, 10), (10, 10)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(100, 100)))
    assert task_func(L).equals(expected_df)

# Test case 5
def test_task_func_5():
    L = [(1, 1), (1, 1)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(1, 1)))
    assert task_func(L).equals(expected_df)

# Test case 6
def test_task_func_6():
    L = [(100, 100), (100, 100)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(10000, 10000)))
    assert task_func(L).equals(expected_df)

# Test case 7
def test_task_func_7():
    L = [(1000, 1000), (1000, 1000)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(1000000, 1000000)))
    assert task_func(L).equals(expected_df)

# Test case 8
def test_task_func_8():
    L = [(10000, 10000), (10000, 10000)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(100000000, 100000000)))
    assert task_func(L).equals(expected_df)

# Test case 9
def test_task_func_9():
    L = [(100000, 100000), (100000, 100000)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(10000000000, 10000000000)))
    assert task_func(L).equals(expected_df)

# Test case 10
def test_task_func_10():
    L = [(1000000, 1000000), (1000000, 1000000)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(1000000000000, 1000000000000)))
    assert task_func(L).equals(expected_df)