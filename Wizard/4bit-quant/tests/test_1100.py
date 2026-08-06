python
import re
from collections import Counter
import pytest

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
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)
    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)
    # Count the frequency of each word
    word_freq = Counter(words)
    result = Counter(words)
    for i in word_freq:
        if i not in PREDEFINED_STOPWORDS:
            del result[i]
    return list(result.items())

def test_task_func():
    # Test case 1
    text = "This is a sample text. It contains some stopwords like me, my, and myself."
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 2
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 3
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 4
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 5
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 6
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 7
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 8
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 9
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result
    
    # Test case 10
    text = "This is a sample text. It contains some stopwords like me, my, and myself. http://www.example.com"
    expected_result = [('sample', 1), ('text', 1), ('contains', 1), ('stopwords', 1)]
    assert task_func(text) == expected_result