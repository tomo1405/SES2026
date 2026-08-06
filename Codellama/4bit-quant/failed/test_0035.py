import pytest
from src_0035 import task_func

def test_task_func():
    # Test with valid input
    text = "This is a sample text for testing the task function."
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)
    assert wordcloud.to_image() is not None

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func("")

    # Test with URL removal
    text = "This is a sample text for testing the task function. http://www.example.com"
    wordcloud = task_func(text)
    assert isinstance(wordcloud, WordCloud)
    assert wordcloud.to_image() is not None