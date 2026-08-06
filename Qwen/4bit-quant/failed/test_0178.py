import pytest
from src_0178 import task_func
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')

@pytest.fixture
def sample_df():
    data = {
        'Title': ['What is AI?', 'Like the weather', 'Unrelated topic'],
        'Content': [
            'Artificial intelligence is a field of study.',
            'I like sunny days.',
            'This article is about something else.'
        ]
    }
    return pd.DataFrame(data)

def test_task_func_with_interesting_titles(sample_df):
    result = task_func(sample_df)
    expected = {'Artificial': 1, 'intelligence': 1, 'is': 2, 'a': 1, 'field': 1, 'of': 1, 'study': 1, 'I': 1, 'sunny': 1, 'days': 1}
    assert result == expected

def test_task_func_without_interesting_titles():
    data = {
        'Title': ['No match here', 'Another unrelated title'],
        'Content': ['This content is irrelevant.', 'So is this one.']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {}

def test_task_func_missing_columns():
    data = {
        'Title': ['What is AI?']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == "DataFrame must include 'Title' and 'Content' columns."

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    result = task_func(df)
    assert result == {}

def test_task_func_punctuation_exclusion():
    data = {
        'Title': ['What is AI?'],
        'Content': ['Punctuation should be excluded!']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    expected = {'Punctuation': 1, 'should': 1, 'be': 1, 'excluded': 1}
    assert result == expected