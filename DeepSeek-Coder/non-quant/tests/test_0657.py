import pytest
from src_0657 import task_func
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Initialize the SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

@pytest.fixture
def setup():
    return sia

def test_task_func(setup):
    sia = setup
    result = task_func("Hello world!", sia)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert 'neg' in result, "The result should contain 'neg' key"
    assert 'neu' in result, "The result should contain 'neu' key"
    assert 'pos' in result, "The result should contain 'pos' key"
    assert 'compound' in result, "The result should contain 'compound' key"