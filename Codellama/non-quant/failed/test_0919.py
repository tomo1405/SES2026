import pytest
from src_0919 import task_func
import pandas as pd

# Test 1: Test that the function returns a DataFrame
def test_returns_dataframe():
    data = [['Hello', 'World'], ['Test', 'Case']]
    mapping = {'Hello': 'Hi', 'World': 'Earth'}
    result = task_func(data, mapping)
    assert isinstance(result, pd.DataFrame)

# Test 2: Test that the function replaces acronyms correctly
def test_replaces_acronyms():
    data = [['Hello', 'World'], ['Test', 'Case']]
    mapping = {'Hello': 'Hi', 'World': 'Earth'}
    result = task_func(data, mapping)
    expected = [['Hi', 'Earth'], ['Test', 'Case']]
    assert result.values.tolist() == expected

# Test 3: Test that the function handles non-string values correctly
def test_handles_non_string_values():
    data = [['Hello', 'World'], ['Test', 'Case']]
    mapping = {'Hello': 'Hi', 'World': 'Earth'}
    result = task_func(data, mapping)
    expected = [['Hi', 'Earth'], ['Test', 'Case']]
    assert result.values.tolist() == expected

# Test 4: Test that the function handles missing values correctly
def test_handles_missing_values():
    data = [['Hello', 'World'], ['Test', 'Case']]
    mapping = {'Hello': 'Hi', 'World': 'Earth'}
    result = task_func(data, mapping)
    expected = [['Hi', 'Earth'], ['Test', 'Case']]
    assert result.values.tolist() == expected

# Test 5: Test that the function handles extra values correctly
def test_handles_extra_values():
    data = [['Hello', 'World'], ['Test', 'Case']]
    mapping = {'Hello': 'Hi', 'World': 'Earth'}
    result = task_func(data, mapping)
    expected = [['Hi', 'Earth'], ['Test', 'Case']]
    assert result.values.tolist() == expected