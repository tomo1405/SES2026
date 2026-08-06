python
import re
from string import punctuation
import pytest

# Predefined list of common stopwords
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}

def task_func(text):
    # Constants
    PUNCTUATION = set(punctuation)

    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Remove punctuation
    text = re.sub('[{}]'.format(re.escape(''.join(PUNCTUATION))), '', text)

    # Tokenize the text
    words = text.split()

    # Remove stopwords
    cleaned_words = [word for word in words if word.lower() not in PREDEFINED_STOPWORDS]

    return ' '.join(cleaned_words)

def test_task_func():
    # Test case 1
    text = "This is a test sentence. It contains some stopwords like me, my, and myself."
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 2
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 3
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 4
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 5
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 6
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 7
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 8
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 9
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output

    # Test case 10
    text = "This is a test sentence. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_output = "test sentence contains stopwords"
    assert task_func(text) == expected_output