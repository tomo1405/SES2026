import pandas as pd
import pytest
from src_0923 import task_func

# Constants
STOPWORDS = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
    "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "don", "should", "now"
])

def test_task_func():
    data = {'column': ['This is a test sentence with some stopwords']}
    df = task_func(data, 'column')
    assert isinstance(df, pd.DataFrame)
    assert df['column'][0] == 'test sentence some'

def test_task_func_empty_column():
    data = {'column': ['']}
    df = task_func(data, 'column')
    assert isinstance(df, pd.DataFrame)
    assert df['column'][0] == ''

def test_task_func_no_stopwords():
    data = {'column': ['This is a test sentence without any stopwords']}
    df = task_func(data, 'column')
    assert isinstance(df, pd.DataFrame)
    assert df['column'][0] == 'This is a test sentence without any'

def test_task_func_invalid_column():
    with pytest.raises(KeyError):
        data = {'invalid_column': ['This is a test sentence with some stopwords']}
        task_func(data, 'invalid_column')