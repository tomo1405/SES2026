import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation
sia = SentimentIntensityAnalyzer()

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    text = ALPHANUMERIC.sub(' ', text).lower()
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def test_task_func():
    text = "This is a test sentence."
    expected_sentiment_scores = sia.polarity_scores("this is a test sentence")
    actual_sentiment_scores = task_func(text, sia)
    assert actual_sentiment_scores == expected_sentiment_scores

def test_task_func_with_punctuation():
    text = "This, is a test! sentence."
    expected_sentiment_scores = sia.polarity_scores("this is a test sentence")
    actual_sentiment_scores = task_func(text, sia)
    assert actual_sentiment_scores == expected_sentiment_scores

def test_task_func_with_numbers():
    text = "This is a test 1 sentence."
    expected_sentiment_scores = sia.polarity_scores("this is a test 1 sentence")
    actual_sentiment_scores = task_func(text, sia)
    assert actual_sentiment_scores == expected_sentiment_scores

def test_task_func_with_special_characters():
    text = "This # is a $ test % sentence."
    expected_sentiment_scores = sia.polarity_scores("this is a test sentence")
    actual_sentiment_scores = task_func(text, sia)
    assert actual_sentiment_scores == expected_sentiment_scores