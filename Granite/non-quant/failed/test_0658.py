import re
import nltk
from gensim.models import Word2Vec
from src_0658 import task_func

def test_task_func():
    texts = ['This is a sample text.', 'Another sample text here.']
    stopwords = nltk.corpus.stopwords.words('english')
    expected_model = Word2Vec(vector_size=100)
    actual_model = task_func(texts, stopwords)
    assert actual_model == expected_model

def test_task_func_with_stopwords():
    texts = ['This is a sample text.', 'Another sample text here.']
    stopwords = ['is', 'a', 'text.']
    expected_model = Word2Vec(sentences=[['sample', 'another', 'sample', 'here.']], vector_size=100, window=5, min_count=1, workers=4)
    actual_model = task_func(texts, stopwords)
    assert actual_model.wv.vocab == expected_model.wv.vocab

def test_task_func_with_empty_texts():
    texts = []
    expected_model = Word2Vec(vector_size=100)
    actual_model = task_func(texts)
    assert actual_model == expected_model