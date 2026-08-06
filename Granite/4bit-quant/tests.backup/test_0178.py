import re
import nltk
import pandas as pd
from string import punctuation
from src_0178 import task_func

def test_task_func_df_columns():
    df = pd.DataFrame({"Title": ["Test Title"], "Content": ["Test Content"]})
    with pytest.raises(ValueError) as exc_info:
        task_func(df)
    assert "DataFrame must include 'Title' and 'Content' columns." in str(exc_info.value)

def test_task_func_interesting_articles():
    df = pd.DataFrame({"Title": ["Test Title"], "Content": ["Test Content"]})
    word_freq = task_func(df)
    assert word_freq == {}

def test_task_func_word_freq():
    df = pd.DataFrame({"Title": ["Test Title"], "Content": ["Test Content like"]})
    word_freq = task_func(df)
    assert word_freq == {"like": 1}