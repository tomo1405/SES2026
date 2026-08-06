import pytest
from src_0180 import task_func

def test_task_func_with_valid_data():
    df = pd.DataFrame({'Title': ['How to learn Python', 'What is the meaning of life?'], 'Content': ['Python is a popular programming language.', 'The meaning of life is to find your purpose.']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticklabels()[0].get_text() == 'Python'
    assert ax.get_xticklabels()[1].get_text() == 'purpose'

def test_task_func_with_invalid_data():
    df = pd.DataFrame({'Title': ['How to learn Python', 'What is the meaning of life?'], 'Content': ['Python is a popular programming language.', 'The meaning of life is to find your purpose.']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticklabels()[0].get_text() == 'Python'
    assert ax.get_xticklabels()[1].get_text() == 'purpose'

def test_task_func_with_empty_data():
    df = pd.DataFrame({'Title': [], 'Content': []})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticklabels() == []