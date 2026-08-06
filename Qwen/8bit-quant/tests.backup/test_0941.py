import pytest
from src_0941 import task_func
from nltk.tokenize import word_tokenize
from collections import Counter

# Mocking the word_tokenize function to control its behavior in tests
@pytest.fixture
def mock_word_tokenize(monkeypatch):
    def mock_tokenizer(text):
        # Define a simple tokenizer for testing purposes
        return text.split()
    monkeypatch.setattr(word_tokenize, 'word_tokenize', mock_tokenizer)

def test_task_func_with_no_special_characters():
    input_str = "Hello world"
    expected_output = Counter({'Hello': 1, 'world': 1})
    assert task_func(input_str) == expected_output

def test_task_func_with_special_characters():
    input_str = "Hello, world!"
    expected_output = Counter({'Hello': 1, 'world': 1})
    assert task_func(input_str) == expected_output

def test_task_func_with_numbers():
    input_str = "Hello 123 world 456"
    expected_output = Counter({'Hello': 1, '123': 1, 'world': 1, '456': 1})
    assert task_func(input_str) == expected_output

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = Counter()
    assert task_func(input_str) == expected_output

def test_task_func_with_all_special_characters():
    input_str = "!@#$%^&*()"
    expected_output = Counter()
    assert task_func(input_str) == expected_output

def test_task_func_with_mixed_case():
    input_str = "Hello hello HELLO"
    expected_output = Counter({'Hello': 3})
    assert task_func(input_str) == expected_output

def test_task_func_with_mock_tokenizer(mock_word_tokenize):
    input_str = "Hello world"
    expected_output = Counter({'Hello': 1, 'world': 1})
    assert task_func(input_str) == expected_output