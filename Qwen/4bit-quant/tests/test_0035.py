import pytest
from src_0035 import task_func
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_with_urls():
    text_with_urls = "This is a sample text with a URL http://example.com and another https://example.org"
    wordcloud = task_func(text_with_urls)
    assert isinstance(wordcloud, WordCloud)

def test_task_func_no_urls():
    text_no_urls = "This is a sample text without any URLs"
    wordcloud = task_func(text_no_urls)
    assert isinstance(wordcloud, WordCloud)

def test_task_func_empty_text():
    empty_text = ""
    with pytest.raises(ValueError) as excinfo:
        task_func(empty_text)
    assert str(excinfo.value) == "No words available to generate a word cloud after removing URLs."

def test_task_func_only_urls():
    only_urls = "http://example.com https://example.org"
    with pytest.raises(ValueError) as excinfo:
        task_func(only_urls)
    assert str(excinfo.value) == "No words available to generate a word cloud after removing URLs."

def test_task_func_whitespace():
    whitespace_text = "   \t\n"
    with pytest.raises(ValueError) as excinfo:
        task_func(whitespace_text)
    assert str(excinfo.value) == "No words available to generate a word cloud after removing URLs."

def test_task_func_plot_display():
    text = "This is a sample text for plotting"
    wordcloud = task_func(text)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64