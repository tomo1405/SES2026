import pytest
from src_0335 import task_func
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

@pytest.fixture
def documents():
    return [
        "The quick brown fox jumps over the lazy dog",
        "Never jump over the lazy dog quickly"
    ]

def test_task_func_output_type(documents):
    result = task_func(documents)
    assert isinstance(result, pd.DataFrame)

def test_task_func_column_names(documents):
    result = task_func(documents)
    expected_columns = set(word_tokenize(" ".join(documents)))
    assert set(result.columns) == expected_columns

def test_task_func_tfidf_values(documents):
    result = task_func(documents)
    assert all(result.values >= 0) and all(result.values <= 1)

def test_task_func_empty_input():
    result = task_func([])
    assert result.empty

def test_task_func_single_document():
    documents = ["The quick brown fox"]
    result = task_func(documents)
    assert len(result.columns) == len(set(word_tokenize(documents[0])))

def test_task_func_duplicate_documents():
    documents = ["Hello world", "Hello world", "Hello world"]
    result = task_func(documents)
    assert len(result.columns) == len(set(word_tokenize(documents[0])))