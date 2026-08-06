import pytest
from src_0335 import task_func
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = ["This is the first document.", "This document is the second document.", "And this is the third one.", "Is this the first document?"]

@pytest.fixture
def mock_word_tokenize():
    def mock_func(text):
        return text.split()
    return mock_func

@pytest.fixture
def mock_TfidfVectorizer():
    class MockVectorizer:
        def fit_transform(self, documents):
            return [[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
        def get_feature_names_out(self):
            return ["feature1", "feature2", "feature3", "feature4"]
    return MockVectorizer

def test_task_func(mock_word_tokenize, mock_TfidfVectorizer):
    vectorizer = TfidfVectorizer(tokenizer=mock_word_tokenize)
    tfidf_matrix = vectorizer.fit_transform(documents)
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

    assert task_func(documents) == tfidf_df