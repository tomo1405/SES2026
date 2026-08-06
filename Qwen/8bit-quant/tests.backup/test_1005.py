import pytest
from src_1005 import task_func
from unittest.mock import patch
from collections import Counter
import matplotlib.pyplot as plt

@patch('urllib.request.urlopen')
def test_task_func(mock_urlopen):
    # Mock the response
    mock_response = mock_urlopen.return_value.__enter__.return_value
    mock_response.read.return_value.decode.return_value = "test text with some words words"

    # Expected output
    expected_words = ["test", "text", "with", "some", "words"]
    expected_word_freq = Counter({"words": 2, "test": 1, "text": 1, "with": 1, "some": 1})
    expected_top_words = [("words", 2), ("test", 1), ("text", 1), ("with", 1), ("some", 1)]

    # Call the function
    word_freq, ax = task_func("http://example.com")

    # Check word frequency
    assert word_freq == expected_word_freq

    # Check top words
    assert word_freq.most_common(10) == expected_top_words

    # Check plot properties
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"
    assert list(ax.patches)[0].get_height() == 2  # First bar height should be 2

    # Clean up plot
    plt.close(ax.get_figure())