import pytest
from src_0733 import task_func
from nltk.stem import PorterStemmer
from collections import Counter

# Mocking the PorterStemmer to avoid external dependency during testing
class MockPorterStemmer:
    def stem(self, word):
        return word

@pytest.fixture
def mock_stemmer(monkeypatch):
    monkeypatch.setattr(PorterStemmer, 'stem', MockPorterStemmer().stem)

def test_task_func_with_empty_string(mock_stemmer):
    assert task_func("") == {}

def test_task_func_with_single_word(mock_stemmer):
    assert task_func("Hello") == {'hello': 1}

def test_task_func_with_multiple_words(mock_stemmer):
    assert task_func("Hello world! Hello again.") == {'hello': 2, 'world': 1, 'again': 1}

def test_task_func_with_punctuation(mock_stemmer):
    assert task_func("Hello, world!") == {'hello': 1, 'world': 1}

def test_task_func_with_uppercase_and_lowercase(mock_stemmer):
    assert task_func("Hello hello") == {'hello': 2}

def test_task_func_with_numbers(mock_stemmer):
    assert task_func("Hello 123 world") == {'hello': 1, 'world': 1}

def test_task_func_with_special_characters(mock_stemmer):
    assert task_func("Hello @world! #python") == {'hello': 1, 'world': 1, 'python': 1}