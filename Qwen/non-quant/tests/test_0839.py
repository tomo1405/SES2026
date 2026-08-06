import pytest
from src_0839 import task_func
import pandas as pd
from nltk.stem import PorterStemmer

@pytest.fixture
def sample_data():
    return pd.Series(["Hello, World!", "This is a test.", "PyTest is great!"])

def test_task_func(sample_data):
    result = task_func(sample_data)
    expected_result = pd.Series(["hello world", "this is a test", "pytest is great"])
    assert result.equals(expected_result)

def test_task_func_empty_string(sample_data):
    sample_data[0] = ""
    result = task_func(sample_data)
    expected_result = pd.Series(["", "this is a test", "pytest is great"])
    assert result.equals(expected_result)

def test_task_func_special_characters(sample_data):
    sample_data[1] = "!!!Special$$$Characters@@@"
    result = task_func(sample_data)
    expected_result = pd.Series(["hello world", "special charact", "pytest is great"])
    assert result.equals(expected_result)

def test_task_func_numbers(sample_data):
    sample_data[2] = "Numbers 1234 and symbols #$%&*"
    result = task_func(sample_data)
    expected_result = pd.Series(["hello world", "this is a test", "number 1234 and symbol"])
    assert result.equals(expected_result)