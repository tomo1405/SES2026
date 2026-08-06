import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation
def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    text = ALPHANUMERIC.sub(' ', text).lower()
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores
import pytest
def test_task_func():
    sia = SentimentIntensityAnalyzer()
    text = "This is a test sentence."
    expected_output = {'neg': 0.0, 'neu': 0.444, 'pos': 0.556, 'compound': 0.5714}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function output does not match expected output"
def test_task_func_with_punctuation():
    sia = SentimentIntensityAnalyzer()
    text = "This, is a test! sentence."
    expected_output = {'neg': 0.0, 'neu': 0.429, 'pos': 0.571, 'compound': 0.5357}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function output does not match expected output"
def test_task_func_with_special_characters():
    sia = SentimentIntensityAnalyzer()
    text = "This #is a $ test^ sentence."
    expected_output = {'neg': 0.0, 'neu': 0.429, 'pos': 0.571, 'compound': 0.5357}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function output does not match expected output"