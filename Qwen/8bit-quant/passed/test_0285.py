import pytest
from src_0285 import task_func
from unittest.mock import patch

@pytest.mark.parametrize("url, expected_links", [
    ("http://example.com", ["http://example.com/page1", "http://example.com/page2"]),
    ("http://testsite.com", ["http://testsite.com/about", "http://testsite.com/contact"]),
])
@patch('src_0285.mechanize.Browser')
def test_task_func(mock_browser, url, expected_links):
    # Mock the response from the browser
    mock_response = mock_browser.return_value.open.return_value
    mock_response.read.return_value = b"""
    <html>
        <body>
            <a href="page1">Page 1</a>
            <a href="page2">Page 2</a>
        </body>
    </html>
    """

    # Call the function
    result = task_func(url)

    # Assert the result
    assert result == expected_links