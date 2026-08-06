python
import re
import string
import pytest

def task_func(content):
    STOPWORDS = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
        "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
        "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
        "these", "those", "is", "are", "was", "were", "be", "been", "being", "have", 
        "has", "had", "having", "do", "does", "did", "doing", "an", "the", "and", 
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
        "for", "with", "about", "against", "between", "into", "through", "during", 
        "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", 
        "on", "off", "over", "under", "again", "further", "then", "once"
    ])

    content = content.split(' ')
    if len(content) > 1:
        content = content[:-1]
    else:
        content = []
    words = [word.strip(string.punctuation).lower() for word in re.split(r'\W+', ' '.join(content)) if word]
    non_stopwords = [word for word in words if word not in STOPWORDS]
    count = len(non_stopwords)

    return count

def test_task_func():
    assert task_func("Hello, world!") == 2
    assert task_func("The quick brown fox jumps over the lazy dog.") == 8
    assert task_func("Python is a great language!") == 4
    assert task_func("I love programming!") == 3
    assert task_func("The cat in the hat.") == 3
    assert task_func("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.") == 16
    assert task_func("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.") == 24