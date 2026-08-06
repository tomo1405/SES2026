import pytest
from src_0919 import task_func

def test_task_func():
    # Test case 1: Replace acronym with existing mapping
    data = {'Column1': ['ABC', 'DEF', 'GHI'], 'Column2': ['XYZ', 'LMN', 'OPQ']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Bravo'}
    expected_output = pd.DataFrame({'Column1': ['Alpha', 'Bravo', 'GHI'], 'Column2': ['XYZ', 'LMN', 'OPQ']})
    assert task_func(data, mapping).equals(expected_output)

    # Test case 2: No acronym to replace
    data = {'Column1': ['abc', 'def', 'ghi'], 'Column2': ['xyz', 'lmn', 'opq']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Bravo'}
    expected_output = pd.DataFrame({'Column1': ['abc', 'def', 'ghi'], 'Column2': ['xyz', 'lmn', 'opq']})
    assert task_func(data, mapping).equals(expected_output)

    # Test case 3: Mixed case acronyms
    data = {'Column1': ['Abc', 'Def', 'Ghi'], 'Column2': ['Xyz', 'Lmn', 'Opq']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Bravo'}
    expected_output = pd.DataFrame({'Column1': ['Abc', 'Def', 'Ghi'], 'Column2': ['Xyz', 'Lmn', 'Opq']})
    assert task_func(data, mapping).equals(expected_output)

    # Test case 4: Non-string values in DataFrame
    data = {'Column1': [123, 'ABC', 'GHI'], 'Column2': ['XYZ', 'LMN', 456]}
    mapping = {'ABC': 'Alpha'}
    expected_output = pd.DataFrame({'Column1': [123, 'Alpha', 'GHI'], 'Column2': ['XYZ', 'LMN', 456]})
    assert task_func(data, mapping).equals(expected_output)

    # Test case 5: Empty DataFrame
    data = {}
    mapping = {'ABC': 'Alpha'}
    expected_output = pd.DataFrame()
    assert task_func(data, mapping).equals(expected_output)

    # Test case 6: Empty mapping
    data = {'Column1': ['ABC', 'DEF', 'GHI'], 'Column2': ['XYZ', 'LMN', 'OPQ']}
    mapping = {}
    expected_output = pd.DataFrame({'Column1': ['ABC', 'DEF', 'GHI'], 'Column2': ['XYZ', 'LMN', 'OPQ']})
    assert task_func(data, mapping).equals(expected_output)