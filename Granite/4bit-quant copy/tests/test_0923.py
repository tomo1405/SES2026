import pandas as pd
import re
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
    data = {'col1': ['This is a test sentence.', 'Another test sentence with some stopwords.']}
    df = pd.DataFrame(data)
    df = task_func(data, 'col1')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 1)
    assert df.iloc[0, 0] == 'test sentence'
    assert df.iloc[1, 0] == 'test sentence stopwords'

def test_task_func_empty_column():
    data = {'col1': ['This is a test sentence.', 'Another test sentence with some stopwords.']}
    df = pd.DataFrame(data)
    df = task_func(data, 'col2')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 1)
    assert df.iloc[0, 0] == ''
    assert df.iloc[1, 0] == ''

def test_task_func_empty_data():
    df = task_func({}, 'col1')
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 1)

def test_task_func_invalid_column():
    data = {'col1': ['This is a test sentence.', 'Another test sentence with some stopwords.']}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        task_func(data, 'col3')