import pytest
from src_0919 import task_func
import pandas as pd

def test_task_func_with_no_acronyms():
    data = {'Column1': ['Hello world'], 'Column2': [123]}
    mapping = {}
    expected_output = pd.DataFrame({'Column1': ['Hello world'], 'Column2': [123]})
    assert task_func(data, mapping).equals(expected_output)

def test_task_func_with_single_acronym():
    data = {'Column1': ['ABC is short for Alpha Beta Charlie']}
    mapping = {'ABC': 'Alpha Beta Charlie'}
    expected_output = pd.DataFrame({'Column1': ['Alpha Beta Charlie is short for Alpha Beta Charlie']})
    assert task_func(data, mapping).equals(expected_output)

def test_task_func_with_multiple_acronyms():
    data = {'Column1': ['ABC and DEF are acronyms'], 'Column2': ['GHI stands for Golf Hotel India']}
    mapping = {'ABC': 'Alpha Beta Charlie', 'DEF': 'Delta Echo Foxtrot', 'GHI': 'Golf Hotel India'}
    expected_output = pd.DataFrame({
        'Column1': ['Alpha Beta Charlie and Delta Echo Foxtrot are acronyms'],
        'Column2': ['Golf Hotel India stands for Golf Hotel India']
    })
    assert task_func(data, mapping).equals(expected_output)

def test_task_func_with_mixed_data_types():
    data = {'Column1': ['XYZ is an acronym', 456], 'Column2': ['LMN is also an acronym', 'Not an acronym']}
    mapping = {'XYZ': 'Xylophone Yacht Zeppelin', 'LMN': 'Lemon Melon Nectarine'}
    expected_output = pd.DataFrame({
        'Column1': ['Xylophone Yacht Zeppelin is an acronym', 456],
        'Column2': ['Lemon Melon Nectarine is also an acronym', 'Not an acronym']
    })
    assert task_func(data, mapping).equals(expected_output)

def test_task_func_with_no_matching_acronyms():
    data = {'Column1': ['No acronyms here']}
    mapping = {'ABC': 'Alpha Beta Charlie'}
    expected_output = pd.DataFrame({'Column1': ['No acronyms here']})
    assert task_func(data, mapping).equals(expected_output)