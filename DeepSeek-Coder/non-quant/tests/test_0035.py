import pytest
from src_0035 import task_func
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a sample text
    text = "This is a sample text with a http://example.com link."
    result = task_func(text)
    assert result is not None

    # Add more tests as needed to cover different scenarios