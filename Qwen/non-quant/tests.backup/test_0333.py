import pytest
from src_0333 import task_func
from collections import Counter
from nltk.corpus import stopwords

@pytest.fixture(scope="module")
def setup():
    # Ensure that stopwords are downloaded
    stopwords.ensure_loaded('english')

def test_task_func_empty_string(setup):
    assert task_func("") == {}

def test_task_func_no_non_stopwords(setup):
    text = "a the of and"
    assert task_func(text) == {}

def test_task_func_single_word(setup):
    text = "hello"
    assert task_func(text) == {'hello': 1}

def test_task_func_multiple_words(setup):
    text = "hello world hello"
    assert task_func(text) == {'world': 1, 'hello': 2}

def test_task_func_with_punctuation(setup):
    text = "Hello, world! Hello."
    assert task_func(text) == {'world': 1, 'hello': 2}

def test_task_func_case_insensitivity(setup):
    text = "HELLO hello HeLLo"
    assert task_func(text) == {'hello': 3}

def test_task_func_with_numbers(setup):
    text = "hello 123 world 456"
    assert task_func(text) == {'hello': 1, 'world': 1}