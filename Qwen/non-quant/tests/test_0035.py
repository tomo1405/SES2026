import pytest
from src_0035 import task_func
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_removes_urls():
    text_with_url = "Check out this link http://example.com and some text."
    expected_text = "Check out this link  and some text."
    assert task_func(text_with_url) == WordCloud().generate(expected_text)

def test_task_func_raises_value_error_on_empty_text_after_url_removal():
    text_with_only_url = "http://example.com"
    with pytest.raises(ValueError, match="No words available to generate a word cloud after removing URLs."):
        task_func(text_with_only_url)

def test_task_func_generates_word_cloud():
    text = "This is a simple test text for generating a word cloud."
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)

def test_task_func_plot():
    text = "This is a simple test text for generating a word cloud."
    wordcloud = task_func(text)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64  # Ensure that the image is generated and not empty