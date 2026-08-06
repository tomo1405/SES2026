import pandas as pd
import pytest
from src_0180 import task_func


def test_task_func():
    df = pd.DataFrame({'Title': ['How to Train Your Dragon', 'What to Wear', 'How to Cook'],
                       'Content': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about cooking']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticks() == ['how', 'what']
    assert ax.get_xticklabels() == ['How to Train Your Dragon', 'What to Wear', 'How to Cook']
    assert ax.get_yticks() == [0, 1, 2]
    assert ax.get_yticklabels() == ['0', '1', '2']

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({'Title': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about cooking'],
                       'Content': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about cooking']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticks() == []
    assert ax.get_xticklabels() == []
    assert ax.get_yticks() == []
    assert ax.get_yticklabels() == []

def test_task_func_invalid_input():
    df = pd.DataFrame({'Title': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about cooking'],
                       'Content': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about cooking']})
    with pytest.raises(ValueError):
        task_func(df)