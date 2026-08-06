import pytest
from src_0150 import task_func

def test_task_func_basic():
    elements = ['apple', 'banana', 'cherry']
    result = task_func(elements)
    expected_columns = ['Element', 'Count']
    assert all(col in result.columns for col in expected_columns), "DataFrame does not contain the correct columns"
    assert len(result) == len(elements), "DataFrame length does not match the input list length"
    assert result['Element'].tolist() == elements, "Elements in DataFrame do not match the input list"
    assert result['Count'].tolist() == [len(el) for el in elements], "Counts in DataFrame do not match the lengths of elements"

def test_task_func_with_index():
    elements = ['apple', 'banana', 'cherry']
    result = task_func(elements, include_index=True)
    expected_columns = ['Index', 'Element', 'Count']
    assert all(col in result.columns for col in expected_columns), "DataFrame does not contain the correct columns"
    assert len(result) == len(elements), "DataFrame length does not match the input list length"
    assert result['Element'].tolist() == elements, "Elements in DataFrame do not match the input list"
    assert result['Count'].tolist() == [len(el) for el in elements], "Counts in DataFrame do not match the lengths of elements"
    assert result['Index'].tolist() == list(range(len(elements))), "Indexes in DataFrame do not match the expected range"

def test_task_func_empty_list():
    elements = []
    result = task_func(elements)
    expected_columns = ['Element', 'Count']
    assert all(col in result.columns for col in expected_columns), "DataFrame does not contain the correct columns"
    assert len(result) == 0, "DataFrame length should be 0 for empty input list"

def test_task_func_single_element():
    elements = ['single']
    result = task_func(elements)
    expected_columns = ['Element', 'Count']
    assert all(col in result.columns for col in expected_columns), "DataFrame does not contain the correct columns"
    assert len(result) == 1, "DataFrame length should be 1 for single element input"
    assert result['Element'].iloc[0] == 'single', "Single element in DataFrame does not match the input"
    assert result['Count'].iloc[0] == len('single'), "Count for single element is incorrect"

def test_task_func_special_characters():
    elements = ['@#$', '!!!', '&&&']
    result = task_func(elements)
    expected_columns = ['Element', 'Count']
    assert all(col in result.columns for col in expected_columns), "DataFrame does not contain the correct columns"
    assert len(result) == len(elements), "DataFrame length does not match the input list length"
    assert result['Element'].tolist() == elements, "Elements in DataFrame do not match the input list"
    assert result['Count'].tolist() == [len(el) for el in elements], "Counts in DataFrame do not match the lengths of elements"