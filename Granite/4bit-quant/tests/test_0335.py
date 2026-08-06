import pytest
from src_0335 import task_func
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

@pytest.fixture
def documents():
    return ["This is the first document.", "This document is the second document.", "And this is the third one."]

def test_task_func(documents):
    tfidf_df = task_func(documents)
    assert isinstance(tfidf_df, pd.DataFrame)
    assert tfidf_df.shape == (3, len(vectorizer.get_feature_names_out()))

def test_task_func_output(documents):
    expected_output = pd.DataFrame([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
    tfidf_df = task_func(documents)
    assert tfidf_df.equals(expected_output)