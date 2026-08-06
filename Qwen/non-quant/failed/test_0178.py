import pytest
from src_0178 import task_func
import pandas as pd
import re
from string import punctuation

# Mocking nltk.word_tokenize to avoid downloading the nltk models
def mock_word_tokenize(text):
    return text.split()

# Monkey patch nltk.word_tokenize
nltk.word_tokenize = mock_word_tokenize

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({
        'Title': ['Not interesting title', 'Another uninteresting title'],
        'Content': ['Some content', 'More content']
    })
    result = task_func(df)
    assert result == {}

def test_task_func_with_interesting_articles():
    df = pd.DataFrame({
        'Title': ['What is this?', 'Like this', 'Unrelated title'],
        'Content': ['This is a test content.', 'Another test content with like.', 'Irrelevant content.']
    })
    result = task_func(df)
    expected_result = {
        'This': 2,
        'is': 2,
        'a': 1,
        'test': 2,
        'content': 2,
        'Another': 1,
        'with': 1,
        'like': 1,
        'Irrelevant': 1,
        'content.': 1
    }
    assert result == expected_result

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'Title': ['What is this?'],
        'Description': ['Some description']
    })
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == "DataFrame must include 'Title' and 'Content' columns."

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    result = task_func(df)
    assert result == {}

def test_task_func_punctuation_exclusion():
    df = pd.DataFrame({
        'Title': ['What is this?'],
        'Content': ['This is a test content!']
    })
    result = task_func(df)
    assert '!' not in result