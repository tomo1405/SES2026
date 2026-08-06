import pytest
from src_0035 import task_func


def test_task_func_valid_input():
    text = "This is a sample text for testing the word cloud generation."
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)

def test_task_func_invalid_input():
    text = ""
    with pytest.raises(ValueError):
        task_func(text)

def test_task_func_url_removal():
    text = "This is a sample text for testing the word cloud generation. http://www.example.com"
    wordcloud = task_func(text)
    assert "http" not in wordcloud.to_html()

def test_task_func_word_cloud_generation():
    text = "This is a sample text for testing the word cloud generation."
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)
    assert wordcloud.to_html() != ""

def test_task_func_axis_removal():
    text = "This is a sample text for testing the word cloud generation."
    wordcloud = task_func(text)
    assert wordcloud.to_html() != ""
    assert "axis" not in wordcloud.to_html()