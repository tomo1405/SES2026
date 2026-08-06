import pytest
from src_0183 import task_func
import pandas as pd

def test_task_func_no_interesting_articles():
    data = {
        'Title': ['Article about weather', 'News on sports'],
        'Content': ['Weather update today', 'Sports highlights']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == []

def test_task_func_with_interesting_articles():
    data = {
        'Title': ['How to cook pizza', 'What is AI?', 'Weather forecast'],
        'Content': ['Pizza recipe', 'Introduction to AI', 'Today\'s weather']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, list)
    assert len(result) == 2  # Only two articles match the pattern

def test_task_func_single_interesting_article():
    data = {
        'Title': ['What is the meaning of life?'],
        'Content': ['Philosophical discussion on life']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, list)
    assert len(result) == 1

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    result = task_func(df)
    assert result == []