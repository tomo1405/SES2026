import pytest
from src_0809 import task_func
from textblob import Sentiment

def test_task_func_empty_string():
    assert task_func("") == Sentiment(polarity=0.0, subjectivity=0.0)

def test_task_func_single_word_stopword():
    assert task_func("the") == Sentiment(polarity=0.0, subjectivity=0.0)

def test_task_func_single_word_not_stopword():
    result = task_func("hello")
    assert isinstance(result, Sentiment)
    assert result.polarity == 0.0  # "hello" is neutral
    assert result.subjectivity > 0.0  # "hello" is somewhat subjective

def test_task_func_sentence_with_stopwords():
    result = task_func("this is a test sentence")
    assert isinstance(result, Sentiment)
    assert result.polarity == 0.0  # "test" is neutral
    assert result.subjectivity > 0.0  # "test" is somewhat subjective

def test_task_func_sentence_with_repeated_words():
    result = task_func("this this is a test test sentence sentence")
    assert isinstance(result, Sentiment)
    assert result.polarity == 0.0  # "test" is neutral
    assert result.subjectivity > 0.0  # "test" is somewhat subjective

def test_task_func_sentence_with_punctuation():
    result = task_func("This is a test, sentence!")
    assert isinstance(result, Sentiment)
    assert result.polarity == 0.0  # "test" is neutral
    assert result.subjectivity > 0.0  # "test" is somewhat subjective

def test_task_func_negative_sentence():
    result = task_func("I hate this")
    assert isinstance(result, Sentiment)
    assert result.polarity < 0.0  # Negative sentiment
    assert result.subjectivity > 0.0  # Subjective

def test_task_func_positive_sentence():
    result = task_func("I love this")
    assert isinstance(result, Sentiment)
    assert result.polarity > 0.0  # Positive sentiment
    assert result.subjectivity > 0.0  # Subjective