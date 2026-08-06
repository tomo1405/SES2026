import pandas as pd
from src_0183 import task_func


def test_task_func():
    df = pd.DataFrame({'Title': ['How to learn Python', 'What is the meaning of life?', 'How to eat pizza'],
                       'Content': ['Python is a programming language', 'The meaning of life is to find purpose', 'Pizza is a delicious food']})
    expected_output = [0, 1, 0]
    assert task_func(df) == expected_output

def test_task_func_empty_df():
    df = pd.DataFrame({'Title': [], 'Content': []})
    expected_output = []
    assert task_func(df) == expected_output

def test_task_func_no_interesting_articles():
    df = pd.DataFrame({'Title': ['This is not an interesting article', 'This is not an interesting article either'],
                       'Content': ['This is not an interesting article', 'This is not an interesting article either']})
    expected_output = []
    assert task_func(df) == expected_output