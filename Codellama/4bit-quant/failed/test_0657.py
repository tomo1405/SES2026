import pytest
from src_0657 import task_func

@pytest.fixture
def sia():
    return SentimentIntensityAnalyzer()

def test_task_func_positive_sentiment(sia):
    text = "This is a positive sentence."
    expected_scores = {'pos': 1.0, 'neu': 0.0, 'neg': 0.0}
    assert task_func(text, sia) == expected_scores

def test_task_func_negative_sentiment(sia):
    text = "This is a negative sentence."
    expected_scores = {'pos': 0.0, 'neu': 0.0, 'neg': 1.0}
    assert task_func(text, sia) == expected_scores

def test_task_func_neutral_sentiment(sia):
    text = "This is a neutral sentence."
    expected_scores = {'pos': 0.0, 'neu': 1.0, 'neg': 0.0}
    assert task_func(text, sia) == expected_scores

def test_task_func_mixed_sentiment(sia):
    text = "This is a mixed sentence."
    expected_scores = {'pos': 0.5, 'neu': 0.5, 'neg': 0.0}
    assert task_func(text, sia) == expected_scores

def test_task_func_empty_sentence(sia):
    text = ""
    expected_scores = {'pos': 0.0, 'neu': 0.0, 'neg': 0.0}
    assert task_func(text, sia) == expected_scores

def test_task_func_invalid_sentence(sia):
    text = "This is an invalid sentence."
    expected_scores = {'pos': 0.0, 'neu': 0.0, 'neg': 0.0}
    assert task_func(text, sia) == expected_scores