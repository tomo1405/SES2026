import re
import nltk
from gensim.models import Word2Vec
from src_0658 import task_func

def test_task_func():
    texts = ["This is a test sentence.", "Another test sentence!"]
    stopwords = nltk.corpus.stopwords.words('english')
    expected_tokenized_texts = [
        ["test", "sentence"],
        ["another", "test", "sentence"]
    ]
    expected_model = Word2Vec(vector_size=100)

    tokenized_texts, model = task_func(texts, stopwords)

    assert tokenized_texts == expected_tokenized_texts
    assert model == expected_model

def test_task_func_empty_texts():
    texts = []
    stopwords = nltk.corpus.stopwords.words('english')
    expected_tokenized_texts = []
    expected_model = Word2Vec(vector_size=100)

    tokenized_texts, model = task_func(texts, stopwords)

    assert tokenized_texts == expected_tokenized_texts
    assert model == expected_model