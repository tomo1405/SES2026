import re
from collections import Counter
from pytest import mark

def task_func(text, top_n):
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq.most_common(top_n)

@mark.parametrize("text, top_n, expected_output", [
    ("This is a sample text", 2, [("a", 1), ("is", 1)]),
    ("This is another sample text", 3, [("a", 1), ("is", 1), ("another", 1)]),
    ("This is a sample text with some URLs http://example.com and http://test.com", 1, [("a", 1)]),
])
def test_task_func(text, top_n, expected_output):
    assert task_func(text, top_n) == expected_output