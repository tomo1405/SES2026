import nltk
import re
from collections import Counter
from pytest import mark

# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(text):
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word not in STOPWORDS and word != '']
    word_freq = dict(Counter(words))

    return word_freq

@mark.parametrize("text, expected_output", [
    ("This is a test", {"this": 1, "is": 1, "a": 1, "test": 1}),
    ("This is another test", {"this": 1, "is": 1, "another": 1, "test": 1}),
    ("This is a different test", {"this": 1, "is": 1, "different": 1, "test": 1}),
])
def test_task_func(text, expected_output):
    assert task_func(text) == expected_output