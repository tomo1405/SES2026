import pytest
from src_0681 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: No features specified
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    features = []
    expected_output = df
    assert task_func(df, features).equals(expected_output)

    # Test case 2: Features specified
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    features = ['a', 'b']
    expected_output = pd.DataFrame({'a': [0, 0, 0], 'b': [0, 0, 0]})
    assert task_func(df, features).equals(expected_output)

    # Test case 3: Features specified, with dummy column
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'dummy': [0, 0, 0]})
    features = ['a', 'b']
    expected_output = pd.DataFrame({'a': [0, 0, 0], 'b': [0, 0, 0], 'dummy': [0, 0, 0]})
    assert task_func(df, features).equals(expected_output)

    # Test case 4: Features specified, with dummy column, with different index
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    features = ['a', 'b']
    expected_output = pd.DataFrame({'a': [0, 0, 0], 'b': [0, 0, 0], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    assert task_func(df, features).equals(expected_output)

    # Test case 5: Features specified, with dummy column, with different index, with different column order
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    features = ['b', 'a']
    expected_output = pd.DataFrame({'b': [0, 0, 0], 'a': [0, 0, 0], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    assert task_func(df, features).equals(expected_output)

    # Test case 6: Features specified, with dummy column, with different index, with different column order, with different data type
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    features = ['b', 'a']
    expected_output = pd.DataFrame({'b': [0, 0, 0], 'a': [0, 0, 0], 'dummy': [0, 0, 0]}, index=[1, 2, 3])
    assert task_func(df, features).equals(expected_output)