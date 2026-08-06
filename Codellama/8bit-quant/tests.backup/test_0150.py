import pytest
from src_0150 import task_func

def test_task_func():
    elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    include_index = True
    expected_df = pd.DataFrame({'Index': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                              'Element': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
                              'Count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    actual_df = task_func(elements, include_index)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_no_index():
    elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    include_index = False
    expected_df = pd.DataFrame({'Element': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
                              'Count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    actual_df = task_func(elements, include_index)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_empty_elements():
    elements = []
    include_index = True
    expected_df = pd.DataFrame({'Index': [],
                              'Element': [],
                              'Count': []})
    actual_df = task_func(elements, include_index)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_empty_elements_no_index():
    elements = []
    include_index = False
    expected_df = pd.DataFrame({'Element': [],
                              'Count': []})
    actual_df = task_func(elements, include_index)
    pd.testing.assert_frame_equal(actual_df, expected_df)