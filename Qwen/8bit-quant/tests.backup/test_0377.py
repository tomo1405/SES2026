import pytest
from src_0377 import task_func
import nltk
from collections import Counter

# Mocking the stopwords to avoid downloading the NLTK corpus
nltk.download('stopwords')
STOPWORDS = nltk.corpus.stopwords.words('english')

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_single_word():
    result = task_func("Hello")
    assert result == {'hello': 1}

def test_task_func_multiple_words():
    result = task_func("Hello world, hello everyone!")
    assert result == {'hello': 2, 'world': 1, 'everyone': 1}

def test_task_func_with_stopwords():
    result = task_func("This is a test. This test is only a test.")
    assert result == {'test': 3, 'only': 1}

def test_task_func_with_numbers():
    result = task_func("The price is 100 dollars.")
    assert result == {'the': 1, 'price': 1, 'is': 1, 'dollars': 1}

def test_task_func_punctuation():
    result = task_func("Hello, world! Hello; world?")
    assert result == {'hello': 2, 'world': 2}