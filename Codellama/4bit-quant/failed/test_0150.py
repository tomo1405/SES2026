import pytest
from src_0150 import task_func

def test_task_func():
    elements = ['A', 'B', 'C']
    include_index = False
    expected_result = pd.DataFrame({'Element': ['A', 'B', 'C'], 'Count': [1, 1, 1]})
    result = task_func(elements, include_index)
    assert result.equals(expected_result)

def test_task_func_with_index():
    elements = ['A', 'B', 'C']
    include_index = True
    expected_result = pd.DataFrame({'Index': [0, 1, 2], 'Element': ['A', 'B', 'C'], 'Count': [1, 1, 1]})
    result = task_func(elements, include_index)
    assert result.equals(expected_result)

def test_task_func_with_different_elements():
    elements = ['A', 'B', 'C', 'D']
    include_index = False
    expected_result = pd.DataFrame({'Element': ['A', 'B', 'C', 'D'], 'Count': [1, 1, 1, 1]})
    result = task_func(elements, include_index)
    assert result.equals(expected_result)

def test_task_func_with_different_elements_and_index():
    elements = ['A', 'B', 'C', 'D']
    include_index = True
    expected_result = pd.DataFrame({'Index': [0, 1, 2, 3], 'Element': ['A', 'B', 'C', 'D'], 'Count': [1, 1, 1, 1]})
    result = task_func(elements, include_index)
    assert result.equals(expected_result)