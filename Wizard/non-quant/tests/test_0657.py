python
import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation

def test_task_func():
    sia = SentimentIntensityAnalyzer()
    text = "I am happy today!"
    expected_result = {'neg': 0.0, 'neu': 0.254, 'pos': 0.746, 'compound': 0.5793}
    assert task_func(text, sia) == expected_result

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    text = ALPHANUMERIC.sub(' ', text).lower()
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores