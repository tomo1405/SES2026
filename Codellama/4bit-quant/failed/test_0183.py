import pytest
from src_0183 import task_func

def test_task_func():
    df = pd.DataFrame({'Title': ['How to Train Your Dragon', 'What to Wear', 'How to Train Your Dragon 2'],
                       'Content': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about a dragon']})
    expected_output = [0, 1, 0]
    assert task_func(df) == expected_output

def test_task_func_empty_df():
    df = pd.DataFrame({'Title': [], 'Content': []})
    expected_output = []
    assert task_func(df) == expected_output

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({'Title': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about a dragon'],
                       'Content': ['This is a story about a dragon', 'This is a story about fashion', 'This is a story about a dragon']})
    expected_output = []
    assert task_func(df) == expected_output