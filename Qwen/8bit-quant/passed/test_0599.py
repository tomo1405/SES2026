import pytest
from src_0599 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'Word': ['apple', 'banana', 'apricot', 'cherry', 'avocado', 'berry']
    }
    return data

def test_task_func_with_valid_letter(sample_data):
    df = pd.DataFrame(sample_data)
    letter = 'a'
    result = task_func(df, letter)
    expected_result = {5: 2, 6: 1}
    assert result == expected_result

def test_task_func_with_no_matching_words(sample_data):
    df = pd.DataFrame(sample_data)
    letter = 'z'
    result = task_func(df, letter)
    expected_result = {}
    assert result == expected_result

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    result = task_func(df, letter)
    expected_result = {}
    assert result == expected_result

def test_task_func_with_non_string_column(sample_data):
    df = pd.DataFrame(sample_data)
    df['Word'] = df['Word'].astype(object)
    letter = 'a'
    result = task_func(df, letter)
    expected_result = {5: 2, 6: 1}
    assert result == expected_result

def test_task_func_with_invalid_letter(sample_data):
    df = pd.DataFrame(sample_data)
    letter = '1'  # Invalid letter, should be treated as no match
    result = task_func(df, letter)
    expected_result = {}
    assert result == expected_result