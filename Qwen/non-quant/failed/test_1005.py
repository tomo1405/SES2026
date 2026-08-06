import pytest
from src_1005 import task_func
from unittest.mock import patch, MagicMock
from collections import Counter
import matplotlib.pyplot as plt

@pytest.fixture
def mock_response():
    mock_response = MagicMock()
    mock_response.read.return_value = b"Hello world hello"
    return mock_response

@patch('urllib.request.urlopen')
def test_task_func(mock_urlopen, mock_response):
    mock_urlopen.return_value = mock_response
    url = "http://example.com"
    word_freq, ax = task_func(url)

    assert isinstance(word_freq, Counter)
    assert word_freq == Counter({'hello': 2, 'world': 1})

    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Top 10 Most Common Words"
    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"

    bars = ax.patches
    assert len(bars) == 2
    assert bars[0].get_height() == 2
    assert bars[1].get_height() == 1
    assert bars[0].get_x() == 0
    assert bars[1].get_x() == 1

    labels = [label.get_text() for label in ax.get_xticklabels()]
    assert labels == ['hello', 'world']