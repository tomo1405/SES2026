python
import pandas as pd
import numpy as np
import pytest

DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    elements_series = pd.Series(elements)
    count_series = elements_series.apply(lambda x: len(x))
    data_dict = {'Element': elements_series, 'Count': count_series}
    if include_index:
        data_dict['Index'] = np.arange(len(elements))
    count_df = pd.DataFrame(data_dict)
    if include_index:
        count_df = count_df[['Index', 'Element', 'Count']]  # Reordering columns to put 'Index' first
    return count_df

def test_task_func():
    # Test case 1: normal usage
    elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    expected_df = pd.DataFrame({'Element': elements, 'Count': [5, 6, 6, 5, 10]}, columns=DEFAULT_COLUMNS)
    assert task_func(elements) == expected_df

    # Test case 2: include index
    elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    expected_df = pd.DataFrame({'Index': [0, 1, 2, 3, 4], 'Element': elements, 'Count': [5, 6, 6, 5, 10]}, columns=['Index', 'Element', 'Count'])
    assert task_func(elements, include_index=True) == expected_df

    # Test case 3: empty list
    elements = []
    expected_df = pd.DataFrame({'Element': [], 'Count': []}, columns=DEFAULT_COLUMNS)
    assert task_func(elements) == expected_df

    # Test case 4: single element list
    elements = ['apple']
    expected_df = pd.DataFrame({'Element': elements, 'Count': [5]}, columns=DEFAULT_COLUMNS)
    assert task_func(elements) == expected_df

    # Test case 5: multiple element list with duplicates
    elements = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'apple', 'banana', 'cherry', 'date', 'elderberry']
    expected_df = pd.DataFrame({'Element': ['apple', 'banana', 'cherry', 'date', 'elderberry'], 'Count': [5, 6, 6, 5, 10]}, columns=DEFAULT_COLUMNS)
    assert task_func(elements) == expected_df