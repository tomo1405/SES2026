import pytest
from src_0658 import task_func
import nltk
from gensim.models import Word2Vec

# Ensure that the stopwords are available
nltk.download('stopwords')

def test_task_func_no_input():
    model = task_func([])
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_single_text():
    texts = ["This is a test sentence."]
    model = task_func(texts)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100
    assert "test" in model.wv.key_to_index

def test_task_func_multiple_texts():
    texts = ["This is a test sentence.", "Another test sentence here."]
    model = task_func(texts)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100
    assert "test" in model.wv.key_to_index
    assert "sentence" in model.wv.key_to_index

def test_task_func_with_stopwords():
    texts = ["This is a test sentence.", "Another test sentence here."]
    stopwords = ["this", "is", "a", "here"]
    model = task_func(texts, stopwords=stopwords)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100
    assert "test" in model.wv.key_to_index
    assert "sentence" in model.wv.key_to_index
    assert "this" not in model.wv.key_to_index

def test_task_func_non_alphanumeric():
    texts = ["Hello, world!", "123 test 456."]
    model = task_func(texts)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100
    assert "hello" in model.wv.key_to_index
    assert "world" in model.wv.key_to_index
    assert "test" in model.wv.key_to_index
    assert "123" not in model.wv.key_to_index
    assert "456" not in model.wv.key_to_index