import pytest
from src_0335 import task_func
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from nltk.tokenize import word_tokenize

@pytest.fixture
def sample_documents():
    return [
        "The quick brown fox jumps over the lazy dog",
        "Never jump over the lazy dog quickly"
    ]

def test_task_func_output_type(sample_documents):
    result = task_func(sample_documents)
    assert isinstance(result, pd.DataFrame)

def test_task_func_column_names(sample_documents):
    result = task_func(sample_documents)
    expected_columns = set(word_tokenize(" ".join(sample_documents)))
    assert set(result.columns) == expected_columns

def test_task_func_tfidf_values(sample_documents):
    result = task_func(sample_documents)
    assert result.notnull().values.all()

def test_task_func_empty_input():
    result = task_func([])
    assert result.empty

def test_task_func_single_document():
    documents = ["The quick brown fox jumps over the lazy dog"]
    result = task_func(documents)
    assert len(result.columns) == len(word_tokenize(documents[0]))

def test_task_func_duplicate_documents():
    documents = ["The quick brown fox", "The quick brown fox"]
    result = task_func(documents)
    assert (result.iloc[0] == result.iloc[1]).all()