import pytest
from src_0377 import task_func

# Mocking the nltk.corpus.stopwords.words to avoid external dependency
from unittest.mock import patch
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
             'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
             'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
             'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
             'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
             'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
             'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should',
             "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
             'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
             'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
             'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

@patch('src_0377.STOPWORDS', STOPWORDS)
def test_task_func():
    # Test case 1: Basic functionality
    text = "This is a simple test."
    expected_output = {'simple': 1, 'test': 1}
    assert task_func(text) == expected_output

    # Test case 2: Case insensitivity
    text = "This IS a SIMPLE test."
    expected_output = {'simple': 1, 'test': 1}
    assert task_func(text) == expected_output

    # Test case 3: Punctuation handling
    text = "This is a simple test, with punctuation!"
    expected_output = {'simple': 1, 'test': 1, 'with': 1, 'punctuation': 1}
    assert task_func(text) == expected_output

    # Test case 4: Stopwords removal
    text = "This is a test with some stopwords like the and a."
    expected_output = {'test': 1, 'stopwords': 1, 'like': 1, 'some': 1}
    assert task_func(text) == expected_output

    # Test case 5: Empty string
    text = ""
    expected_output = {}
    assert task_func(text) == expected_output

    # Test case 6: Only stopwords
    text = "a the and"
    expected_output = {}
    assert task_func(text) == expected_output