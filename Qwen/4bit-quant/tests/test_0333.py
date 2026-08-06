import pytest
from src_0333 import task_func
from nltk.corpus import stopwords

@pytest.fixture(scope="module")
def setup():
    # Ensure that the stopwords are downloaded
    import nltk
    nltk.download('stopwords')

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_only_stopwords():
    result = task_func("and the of is in at to")
    assert result == {}

def test_task_func_single_word():
    result = task_func("hello")
    assert result == {'hello': 1}

def test_task_func_multiple_words():
    result = task_func("hello world hello")
    assert result == {'hello': 2, 'world': 1}

def test_task_func_case_insensitivity():
    result = task_func("Hello hello HELLO")
    assert result == {'hello': 3}

def test_task_func_with_punctuation():
    result = task_func("Hello, world! Hello...")
    assert result == {'hello': 2, 'world': 1}

def test_task_func_with_numbers():
    result = task_func("Hello 123 world")
    assert result == {'hello': 1, 'world': 1}

def test_task_func_with_special_characters():
    result = task_func("Hello @world! #hello")
    assert result == {'hello': 2, 'world': 1}