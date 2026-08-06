python
import re
from nltk.corpus import stopwords
from collections import Counter
import pytest

STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    lines = input_string.split('\n')
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)

def test_task_func():
    input_string = "This is a sample text.\nThis is another sample text.\nThis is yet another sample text."
    expected_output = {'sample': 3, 'text': 3}
    assert task_func(input_string) == expected_output