import pytest
from src_0657 import task_func
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@pytest.fixture
def sia():
    return SentimentIntensityAnalyzer()

def test_task_func_positive_sentiment(sia):
    text = "I love this product! It works great."
    expected = {'neg': 0.0, 'neu': 0.25, 'pos': 0.75, 'compound': 0.8339}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_negative_sentiment(sia):
    text = "This is the worst product I have ever used!"
    expected = {'neg': 0.75, 'neu': 0.25, 'pos': 0.0, 'compound': -0.8339}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_neutral_sentiment(sia):
    text = "It's just okay."
    expected = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_with_punctuation(sia):
    text = "Wow!!! This is amazing!!!"
    expected = {'neg': 0.0, 'neu': 0.25, 'pos': 0.75, 'compound': 0.8339}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_with_special_characters(sia):
    text = "Th!s @#is &* a t3st."
    expected = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_empty_string(sia):
    text = ""
    expected = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    result = task_func(text, sia)
    assert result == expected

def test_task_func_all_uppercase(sia):
    text = "THIS IS A TEST!"
    expected = {'neg': 0.0, 'neu': 0.25, 'pos': 0.75, 'compound': 0.8339}
    result = task_func(text, sia)
    assert result == expected