import pytest
from src_0335 import task_func
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = ["This is the first document.", "This document is the second document.", "And this is the third one.", "Is this the first document?"]

@pytest.fixture
def input_data():
    return documents

def test_task_func(input_data):
    tfidf_df = task_func(input_data)
    assert isinstance(tfidf_df, pd.DataFrame), "The output should be a pandas DataFrame"
    assert tfidf_df.shape[1] > 0, "The DataFrame should have at least one column"
    assert tfidf_df.shape[0] == len(input_data), "The number of rows in the DataFrame should match the number of input documents"

def test_task_func_with_custom_tokenizer(input_data):
    custom_tokenizer = lambda text: text.split()
    tfidf_df = task_func(input_data, tokenizer=custom_tokenizer)
    assert isinstance(tfidf_df, pd.DataFrame), "The output should be a pandas DataFrame"
    assert tfidf_df.shape[1] > 0, "The DataFrame should have at least one column"
    assert tfidf_df.shape[0] == len(input_data), "The number of rows in the DataFrame should match the number of input documents"