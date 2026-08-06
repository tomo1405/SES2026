import pytest
from src_0657 import task_func
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@pytest.fixture
def sia():
    return SentimentIntensityAnalyzer()

def test_task_func_positive_sentiment(sia):
    text = "I love this product!"
    expected = {'neg': 0.0, 'neu': 0.253, 'pos': 0.747, 'compound': 0.6881}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_negative_sentiment(sia):
    text = "This is the worst experience ever."
    expected = {'neg': 0.747, 'neu': 0.253, 'pos': 0.0, 'compound': -0.6881}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_neutral_sentiment(sia):
    text = "It's okay."
    expected = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_empty_string(sia):
    text = ""
    expected = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_punctuation(sia):
    text = "Hello, world!!!"
    expected = {'neg': 0.0, 'neu': 0.75, 'pos': 0.25, 'compound': 0.25}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_case_insensitivity(sia):
    text = "THIS IS A TEST."
    expected = {'neg': 0.0, 'neu': 0.75, 'pos': 0.25, 'compound': 0.25}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_alphanumeric_removal(sia):
    text = "Hello123! @world$%^&*()"
    expected = {'neg': 0.0, 'neu': 0.75, 'pos': 0.25, 'compound': 0.25}
    result = task_func(text, sia)
    assert result == expected