import pytest
from src_0060 import task_func
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

@patch('wikipedia.page')
def test_task_func_success(mock_wikipedia_page):
    # Mocking the Wikipedia page content
    mock_page = MagicMock()
    mock_page.content = "This is a sample text for testing."
    mock_wikipedia_page.return_value = mock_page

    # Call the function with a mock page title
    result = task_func("Test Page")

    # Assert that the function returns a matplotlib Axes object
    assert isinstance(result, plt.Axes)

@patch('wikipedia.page')
def test_task_func_failure(mock_wikipedia_page):
    # Simulate an exception when fetching the Wikipedia page
    mock_wikipedia_page.side_effect = Exception("Page not found")

    # Call the function with a mock page title
    result = task_func("Nonexistent Page")

    # Assert that the function returns None
    assert result is None

@patch('wikipedia.page')
def test_task_func_empty_content(mock_wikipedia_page):
    # Mocking the Wikipedia page with empty content
    mock_page = MagicMock()
    mock_page.content = ""
    mock_wikipedia_page.return_value = mock_page

    # Call the function with a mock page title
    result = task_func("Empty Page")

    # Assert that the function returns a matplotlib Axes object even with empty content
    assert isinstance(result, plt.Axes)