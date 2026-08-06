import pytest
from src_0656 import task_func

# Mocking dependencies
class MockTfidfVectorizer:
    def __init__(self, max_df=1.0, min_df=1, stop_words='english'):
        self.max_df = max_df
        self.min_df = min_df
        self.stop_words = stop_words
        self.vocabulary_ = {'word1': 0, 'word2': 1, 'word3': 2}

    def fit_transform(self, texts):
        return [[0.1, 0.2, 0.7], [0.8, 0.1, 0.1]]

    def get_feature_names_out(self):
        return ['word1', 'word2', 'word3']

class MockNMF:
    def __init__(self, n_components, random_state=1):
        self.n_components = n_components
        self.random_state = random_state

    def fit(self, tfidf):
        return self

    @property
    def components_(self):
        return [[0.9, 0.05, 0.05], [0.05, 0.9, 0.05]]

@pytest.fixture
def mock_dependencies(monkeypatch):
    monkeypatch.setattr('src_0656.TfidfVectorizer', MockTfidfVectorizer)
    monkeypatch.setattr('src_0656.NMF', MockNMF)

def test_task_func_with_empty_input():
    texts = []
    num_topics = 2
    result = task_func(texts, num_topics)
    assert result == ([], None)

def test_task_func_with_no_valid_tokens(mock_dependencies):
    texts = ["", " ", "the quick brown fox"]
    num_topics = 2
    result = task_func(texts, num_topics)
    assert result == ([], None)

def test_task_func_with_valid_input(mock_dependencies):
    texts = ["This is a sample text.", "Another example sentence."]
    num_topics = 2
    result = task_func(texts, num_topics)
    expected_topics = [['word3'], ['word1']]
    assert result == expected_topics

def test_task_func_with_single_topic(mock_dependencies):
    texts = ["This is a sample text.", "Another example sentence."]
    num_topics = 1
    result = task_func(texts, num_topics)
    expected_topics = [['word3']]
    assert result == expected_topics

def test_task_func_with_more_topics_than_words(mock_dependencies):
    texts = ["This is a sample text."]
    num_topics = 3
    result = task_func(texts, num_topics)
    expected_topics = [['word3'], ['word1'], ['word2']]
    assert result == expected_topics