import pytest
from src_0656 import task_func

# Mocking dependencies
import mock
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

@pytest.fixture
def mock_tfidf_vectorizer():
    with mock.patch('src_0656.TfidfVectorizer') as MockTfidfVectorizer:
        instance = MockTfidfVectorizer.return_value
        instance.fit_transform.return_value = mock.Mock()
        yield instance

@pytest.fixture
def mock_nmf():
    with mock.patch('src_0656.NMF') as MockNMF:
        instance = MockNMF.return_value
        instance.components_ = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        yield instance

@pytest.fixture
def mock_get_feature_names_out():
    with mock.patch('src_0656.TfidfVectorizer.get_feature_names_out') as MockGetFeatureNamesOut:
        MockGetFeatureNamesOut.return_value = ['word1', 'word2', 'word3']
        yield MockGetFeatureNamesOut

def test_task_func_empty_texts(mock_tfidf_vectorizer, mock_nmf, mock_get_feature_names_out):
    texts = []
    num_topics = 2
    result = task_func(texts, num_topics)
    assert result == ([], None)

def test_task_func_no_keywords_after_stopwords_removal(mock_tfidf_vectorizer, mock_nmf, mock_get_feature_names_out):
    texts = ["the quick brown fox", "jumps over the lazy dog"]
    num_topics = 2
    with mock.patch('src_0656.STOPWORDS', {'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'}):
        result = task_func(texts, num_topics)
        assert result == ([], None)

def test_task_func_normal_case(mock_tfidf_vectorizer, mock_nmf, mock_get_feature_names_out):
    texts = ["this is a sample text", "another example"]
    num_topics = 2
    result = task_func(texts, num_topics)
    assert len(result) == num_topics
    assert all(isinstance(topic, list) for topic in result)
    assert all(len(topic) > 0 for topic in result)

def test_task_func_with_special_characters(mock_tfidf_vectorizer, mock_nmf, mock_get_feature_names_out):
    texts = ["hello, world!", "goodbye, cruel world!"]
    num_topics = 2
    result = task_func(texts, num_topics)
    assert len(result) == num_topics
    assert all(isinstance(topic, list) for topic in result)
    assert all(len(topic) > 0 for topic in result)