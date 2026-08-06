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