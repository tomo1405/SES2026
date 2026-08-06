import pytest
from src_0658 import task_func
import re
import nltk
from gensim.models import Word2Vec

# Mocking the nltk corpus stopwords
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('english'))

def test_task_func_empty_input():
    result = task_func([])
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100

def test_task_func_single_text():
    text = "This is a sample text."
    result = task_func([text])
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) > 0

def test_task_func_multiple_texts():
    texts = ["This is a sample text.", "Another example here."]
    result = task_func(texts)
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) > 0

def test_task_func_with_stopwords():
    texts = ["This is a sample text.", "Another example here."]
    custom_stopwords = {"this", "is", "a", "here"}
    result = task_func(texts, stopwords=custom_stopwords)
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) > 0

def test_task_func_no_alpha_numeric():
    texts = ["12345", "!@#$%", "123abc"]
    result = task_func(texts)
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) == 0

def test_task_func_with_punctuation():
    texts = ["Hello, world!", "Python is great!"]
    result = task_func(texts)
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) > 0

def test_task_func_with_uppercase():
    texts = ["HELLO WORLD", "PYTHON IS GREAT"]
    result = task_func(texts)
    assert isinstance(result, Word2Vec)
    assert result.vector_size == 100
    assert len(result.wv.key_to_index) > 0