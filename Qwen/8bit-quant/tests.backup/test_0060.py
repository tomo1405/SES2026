import pytest
from src_0060 import task_func
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Mocking the Wikipedia API to avoid actual network calls
@pytest.fixture
def mock_wikipedia_page():
    page_mock = MagicMock()
    page_mock.content = "This is a sample text for testing."
    with patch.object(wikipedia, 'page', return_value=page_mock) as mock_page:
        yield mock_page

def test_task_func_success(mock_wikipedia_page):
    ax = task_func("Sample Page Title")
    assert isinstance(ax, plt.Axes)
    assert mock_wikipedia_page.called_once_with("Sample Page Title")

def test_task_func_failure(mock_wikipedia_page):
    mock_wikipedia_page.side_effect = Exception("Test exception")
    ax = task_func("Sample Page Title")
    assert ax is None
    assert mock_wikipedia_page.called_once_with("Sample Page Title")