import pandas as pd
from src_0150 import task_func


def test_task_func_basic():
    elements = ['a', 'ab', 'abc']
    expected_output = pd.DataFrame({
        'Element': ['a', 'ab', 'abc'],
        'Count': [1, 2, 3]
    })
    result = task_func(elements)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_index():
    elements = ['a', 'ab', 'abc']
    expected_output = pd.DataFrame({
        'Index': [0, 1, 2],
        'Element': ['a', 'ab', 'abc'],
        'Count': [1, 2, 3]
    })
    result = task_func(elements, include_index=True)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_empty_list():
    elements = []
    expected_output = pd.DataFrame(columns=['Element', 'Count'])
    result = task_func(elements)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_empty_list_with_index():
    elements = []
    expected_output = pd.DataFrame(columns=['Index', 'Element', 'Count'])
    result = task_func(elements, include_index=True)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_single_element():
    elements = ['single']
    expected_output = pd.DataFrame({
        'Element': ['single'],
        'Count': [6]
    })
    result = task_func(elements)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_single_element_with_index():
    elements = ['single']
    expected_output = pd.DataFrame({
        'Index': [0],
        'Element': ['single'],
        'Count': [6]
    })
    result = task_func(elements, include_index=True)
    pd.testing.assert_frame_equal(result, expected_output)