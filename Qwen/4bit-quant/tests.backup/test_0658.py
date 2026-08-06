import pytest
from src_0658 import task_func
import nltk
from gensim.models import Word2Vec

@pytest.fixture
def sample_texts():
    return ["Hello, world!", "This is a test.", "Another example sentence."]

@pytest.fixture
def sample_stopwords():
    return set(["this", "is", "a"])

def test_task_func_with_default_stopwords(sample_texts):
    model = task_func(sample_texts)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_custom_stopwords(sample_texts, sample_stopwords):
    model = task_func(sample_texts, stopwords=sample_stopwords)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_empty_input():
    model = task_func([])
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_single_empty_string():
    model = task_func([""])
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_no_alphanumeric_characters():
    model = task_func(["!!!", "@@@", "###"])
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_punctuation_only(sample_texts):
    model = task_func([text.replace(" ", "") for text in sample_texts])
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100

def test_task_func_with_large_text(sample_texts):
    large_texts = [text * 10 for text in sample_texts]
    model = task_func(large_texts)
    assert isinstance(model, Word2Vec)
    assert model.vector_size == 100