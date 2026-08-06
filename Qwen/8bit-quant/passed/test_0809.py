import pytest
from src_0809 import task_func

def test_task_func_with_positive_sentiment():
    text = "I love this product!"
    sentiment = task_func(text)
    assert sentiment.polarity > 0 and sentiment.subjectivity > 0

def test_task_func_with_negative_sentiment():
    text = "I hate this product."
    sentiment = task_func(text)
    assert sentiment.polarity < 0 and sentiment.subjectivity > 0

def test_task_func_with_neutral_sentiment():
    text = "This product is okay."
    sentiment = task_func(text)
    assert sentiment.polarity == 0 and sentiment.subjectivity > 0

def test_task_func_with_empty_text():
    text = ""
    sentiment = task_func(text)
    assert sentiment.polarity == 0 and sentiment.subjectivity == 0

def test_task_func_with_repeated_words():
    text = "Wow wow this is amazing amazing"
    sentiment = task_func(text)
    assert sentiment.polarity > 0 and sentiment.subjectivity > 0

def test_task_func_with_stopwords_only():
    text = "is the of and"
    sentiment = task_func(text)
    assert sentiment.polarity == 0 and sentiment.subjectivity == 0

def test_task_func_with_punctuation():
    text = "Hello, world! How are you?"
    sentiment = task_func(text)
    assert sentiment.polarity > 0 and sentiment.subjectivity > 0

def test_task_func_with_numbers():
    text = "I have 10 apples and 5 oranges."
    sentiment = task_func(text)
    assert sentiment.polarity > 0 and sentiment.subjectivity > 0