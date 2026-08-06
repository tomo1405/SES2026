import pytest
from src_0850 import task_func
from collections import Counter

# Mocking the stopwords.words function to avoid dependency on NLTK data
@pytest.fixture(autouse=True)
def mock_stopwords(mocker):
    mocker.patch('src_0850.stopwords.words', return_value=['the', 'and', 'is'])

def test_task_func_with_empty_input():
    result = task_func('')
    assert result == {}

def test_task_func_with_single_line_no_words():
    result = task_func('   ')
    assert result == {}

def test_task_func_with_single_line_with_words():
    result = task_func('hello world')
    assert result == {'hello': 1, 'world': 1}

def test_task_func_with_multiple_lines_with_words():
    input_string = "hello world\nthis is a test\nhello again"
    result = task_func(input_string)
    assert result == {'hello': 2, 'world': 1, 'this': 1, 'a': 1, 'test': 1, 'again': 1}

def test_task_func_with_stopwords():
    input_string = "the quick brown fox jumps over the lazy dog"
    result = task_func(input_string)
    assert result == {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

def test_task_func_with_punctuation():
    input_string = "Hello, world! This is a test."
    result = task_func(input_string)
    assert result == {'Hello': 1, 'world': 1, 'This': 1, 'is': 1, 'a': 1, 'test': 1}