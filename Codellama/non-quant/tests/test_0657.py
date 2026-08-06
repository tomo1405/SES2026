import pytest
from src_0657 import task_func


@pytest.fixture
def sia():
    return SentimentIntensityAnalyzer()

def test_task_func_positive_sentiment(sia):
    text = "This is a positive sentence."
    sentiment_scores = task_func(text, sia)
    assert sentiment_scores['pos'] > 0
    assert sentiment_scores['neg'] == 0
    assert sentiment_scores['neu'] == 0

def test_task_func_negative_sentiment(sia):
    text = "This is a negative sentence."
    sentiment_scores = task_func(text, sia)
    assert sentiment_scores['pos'] == 0
    assert sentiment_scores['neg'] > 0
    assert sentiment_scores['neu'] == 0

def test_task_func_neutral_sentiment(sia):
    text = "This is a neutral sentence."
    sentiment_scores = task_func(text, sia)
    assert sentiment_scores['pos'] == 0
    assert sentiment_scores['neg'] == 0
    assert sentiment_scores['neu'] > 0

def test_task_func_mixed_sentiment(sia):
    text = "This is a mixed sentence."
    sentiment_scores = task_func(text, sia)
    assert sentiment_scores['pos'] > 0
    assert sentiment_scores['neg'] > 0
    assert sentiment_scores['neu'] > 0