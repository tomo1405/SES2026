import pytest
from src_0919 import task_func
import pandas as pd

def test_task_func_no_acronyms():
    data = {
        'Column1': ['Hello World', 'This is a test'],
        'Column2': [123, 456]
    }
    mapping = {}
    expected_output = pd.DataFrame({
        'Column1': ['Hello World', 'This is a test'],
        'Column2': [123, 456]
    })
    result = task_func(data, mapping)
    assert result.equals(expected_output)

def test_task_func_with_acronyms():
    data = {
        'Column1': ['NASA is exploring space', 'UN is working on peace'],
        'Column2': ['The EU has 27 countries', 'WHO focuses on health']
    }
    mapping = {
        'NASA': 'National Aeronautics and Space Administration',
        'UN': 'United Nations',
        'EU': 'European Union',
        'WHO': 'World Health Organization'
    }
    expected_output = pd.DataFrame({
        'Column1': ['National Aeronautics and Space Administration is exploring space', 'United Nations is working on peace'],
        'Column2': ['The European Union has 27 countries', 'World Health Organization focuses on health']
    })
    result = task_func(data, mapping)
    assert result.equals(expected_output)

def test_task_func_partial_mapping():
    data = {
        'Column1': ['NASA is exploring space', 'UN is working on peace'],
        'Column2': ['The EU has 27 countries', 'WHO focuses on health']
    }
    mapping = {
        'NASA': 'National Aeronautics and Space Administration',
        'UN': 'United Nations'
    }
    expected_output = pd.DataFrame({
        'Column1': ['National Aeronautics and Space Administration is exploring space', 'United Nations is working on peace'],
        'Column2': ['The EU has 27 countries', 'WHO focuses on health']
    })
    result = task_func(data, mapping)
    assert result.equals(expected_output)

def test_task_func_empty_data():
    data = {}
    mapping = {'NASA': 'National Aeronautics and Space Administration'}
    expected_output = pd.DataFrame()
    result = task_func(data, mapping)
    assert result.equals(expected_output)

def test_task_func_non_string_values():
    data = {
        'Column1': [123, 'NASA is exploring space'],
        'Column2': [456, 'UN is working on peace']
    }
    mapping = {
        'NASA': 'National Aeronautics and Space Administration',
        'UN': 'United Nations'
    }
    expected_output = pd.DataFrame({
        'Column1': [123, 'National Aeronautics and Space Administration is exploring space'],
        'Column2': [456, 'United Nations is working on peace']
    })
    result = task_func(data, mapping)
    assert result.equals(expected_output)