import pytest
from src_0286 import task_func

# Mocking the necessary libraries to avoid network calls and external dependencies
from unittest.mock import patch, MagicMock

@patch('src_0286.mechanize.Browser')
def test_task_func(mock_browser):
    # Setup mock objects
    mock_br = MagicMock()
    mock_response = MagicMock()
    mock_soup = MagicMock()

    # Configure mock behavior
    mock_browser.return_value = mock_br
    mock_br.open.return_value = None
    mock_br.select_form.return_value = None
    mock_br.submit.return_value = mock_response
    mock_response.read.return_value = '<html><head><title>Test Title</title></head><body></body></html>'
    mock_soup.title.string = 'Test Title'

    # Call the function with mock data
    url = 'http://example.com'
    form_id = 0
    data = {'field1': 'value1', 'field2': 'value2'}
    result = task_func(url, form_id, data)

    # Assertions
    mock_br.open.assert_called_once_with(url)
    mock_br.select_form.assert_called_once_with(nr=form_id)
    for key, value in data.items():
        assert mock_br[key] == value
    mock_br.submit.assert_called_once()
    assert result == 'Test Title'

@patch('src_0286.mechanize.Browser')
def test_task_func_no_title(mock_browser):
    # Setup mock objects
    mock_br = MagicMock()
    mock_response = MagicMock()
    mock_soup = MagicMock()

    # Configure mock behavior
    mock_browser.return_value = mock_br
    mock_br.open.return_value = None
    mock_br.select_form.return_value = None
    mock_br.submit.return_value = mock_response
    mock_response.read.return_value = '<html><body></body></html>'
    mock_soup.title = None

    # Call the function with mock data
    url = 'http://example.com'
    form_id = 0
    data = {'field1': 'value1', 'field2': 'value2'}
    result = task_func(url, form_id, data)

    # Assertions
    assert result == 'No Title'