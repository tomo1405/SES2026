import pytest
from src_0657 import task_func
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@pytest.fixture
def sia():
    return SentimentIntensityAnalyzer()

def test_task_func_with_positive_text(sia):
    text = "I love this product!"
    expected_output = {'neg': 0.0, 'neu': 0.125, 'pos': 0.875, 'compound': 0.663}
    assert task_func(text, sia) == expected_output

def test_task_func_with_negative_text(sia):
    text = "This is the worst experience ever."
    expected_output = {'neg': 0.814, 'neu': 0.186, 'pos': 0.0, 'compound': -0.782}
    assert task_func(text, sia) == expected_output

def test_task_func_with_neutral_text(sia):
    text = "It's just okay."
    expected_output = {'neg': 0.2, 'neu': 0.6, 'pos': 0.2, 'compound': 0.0}
    assert task_func(text, sia) == expected_output

def test_task_func_with_mixed_text(sia):
    text = "The food was good, but the service was terrible."
    expected_output = {'neg': 0.359, 'neu': 0.344, 'pos': 0.297, 'compound': -0.216}
    assert task_func(text, sia) == expected_output

def test_task_func_with_empty_text(sia):
    text = ""
    expected_output = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    assert task_func(text, sia) == expected_output

def test_task_func_with_punctuation_only(sia):
    text = "!@#$%^&*()_+"
    expected_output = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    assert task_func(text, sia) == expected_output

def test_task_func_with_numbers(sia):
    text = "I have 100 dollars."
    expected_output = {'neg': 0.0, 'neu': 0.75, 'pos': 0.25, 'compound': 0.162}
    assert task_func(text, sia) == expected_output