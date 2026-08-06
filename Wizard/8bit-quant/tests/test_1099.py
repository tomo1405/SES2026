python
import re
from collections import Counter
import pytest

def task_func(text, top_n):
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq.most_common(top_n)

def test_task_func():
    # Test case 1
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = 3
    expected_result = [('test', 1), ('text', 1), ('urls', 1)]
    assert task_func(text, top_n) == expected_result

    # Test case 2
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = 1
    expected_result = [('test', 1)]
    assert task_func(text, top_n) == expected_result

    # Test case 3
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = 5
    expected_result = [('test', 1), ('text', 1), ('urls', 1), ('this', 1), ('is', 1)]
    assert task_func(text, top_n) == expected_result

    # Test case 4
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = 0
    expected_result = []
    assert task_func(text, top_n) == expected_result

    # Test case 5
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = -1
    expected_result = []
    assert task_func(text, top_n) == expected_result

    # Test case 6
    text = "This is a test text with some URLs. http://www.example.com"
    top_n = 10
    expected_result = [('test', 1), ('text', 1), ('urls', 1), ('this', 1), ('is', 1), ('a', 1), ('with', 1), ('some', 1), ('urls', 1), ('http', 1)]
    assert task_func(text, top_n) == expected_result