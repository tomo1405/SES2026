import pytest
from src_0335 import task_func
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from nltk.tokenize import word_tokenize

# Mocking the TfidfVectorizer to avoid actual computation and dependency on NLTK data files
class MockTfidfVectorizer:
    def __init__(self, tokenizer=None):
        self.tokenizer = tokenizer
        self.feature_names = ['mock_feature1', 'mock_feature2']

    def fit_transform(self, documents):
        # Simulate a transformation that returns a mock TF-IDF matrix
        mock_data = [
            [0.1, 0.2],
            [0.2, 0.1]
        ]
        return pd.DataFrame(mock_data)

    def get_feature_names_out(self):
        return self.feature_names

@pytest.fixture
def mock_vectorizer(monkeypatch):
    monkeypatch.setattr(TfidfVectorizer, '__init__', MockTfidfVectorizer.__init__)
    monkeypatch.setattr(TfidfVectorizer, 'fit_transform', MockTfidfVectorizer.fit_transform)
    monkeypatch.setattr(TfidfVectorizer, 'get_feature_names_out', MockTfidfVectorizer.get_feature_names_out)

def test_task_func_with_mock_vectorizer(mock_vectorizer):
    documents = ["This is a test document.", "Another example document."]
    result = task_func(documents)
    
    expected_columns = ['mock_feature1', 'mock_feature2']
    assert list(result.columns) == expected_columns, "The DataFrame columns do not match the expected feature names."
    
    expected_shape = (2, 2)
    assert result.shape == expected_shape, "The DataFrame shape does not match the expected shape."

def test_task_func_with_empty_documents():
    documents = []
    result = task_func(documents)
    
    expected_columns = []
    assert list(result.columns) == expected_columns, "The DataFrame columns should be empty for empty input."
    
    expected_shape = (0, 0)
    assert result.shape == expected_shape, "The DataFrame shape should be (0, 0) for empty input."

def test_task_func_with_single_document():
    documents = ["A single document."]
    result = task_func(documents)
    
    expected_columns = ['mock_feature1', 'mock_feature2']
    assert list(result.columns) == expected_columns, "The DataFrame columns do not match the expected feature names."
    
    expected_shape = (1, 2)
    assert result.shape == expected_shape, "The DataFrame shape does not match the expected shape."