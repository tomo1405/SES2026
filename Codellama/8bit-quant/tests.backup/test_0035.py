import pytest
from src_0035 import task_func

def test_task_func_valid_input():
    text = "This is a sample text for testing the word cloud."
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)

def test_task_func_invalid_input():
    text = ""
    with pytest.raises(ValueError):
        task_func(text)