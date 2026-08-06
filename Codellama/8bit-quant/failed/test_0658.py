import pytest
from src_0658 import task_func

def test_task_func_stopwords_none():
    texts = ['This is a test text', 'This is another test text']
    stopwords = None
    expected_result = Word2Vec(vector_size=100)

    result = task_func(texts, stopwords)

    assert result == expected_result

def test_task_func_stopwords_not_none():
    texts = ['This is a test text', 'This is another test text']
    stopwords = ['a', 'is']
    expected_result = Word2Vec(sentences=[[word for word in text.split() if word not in stopwords] for text in texts], vector_size=100, window=5, min_count=1, workers=4)

    result = task_func(texts, stopwords)

    assert result == expected_result

def test_task_func_empty_texts():
    texts = []
    stopwords = None
    expected_result = Word2Vec(vector_size=100)

    result = task_func(texts, stopwords)

    assert result == expected_result