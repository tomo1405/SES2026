from unittest.mock import Mock, patch

import pytest
from bs4 import BeautifulSoup
from src_1019 import task_func


@pytest.mark.parametrize("url, from_encoding, use_lxml, expected", [
    ("http://example.com", "cp1251", False, True),  # Valid URL, default encoding, default parser
    ("http://example.com", "utf-8", True, True),   # Valid URL, utf-8 encoding, lxml parser
    ("", "cp1251", False, None),                 # Empty URL, default encoding, default parser
    ("http://nonexistenturl.com", "cp1251", False, None),  # Non-existent URL, default encoding, default parser
])
def test_task_func(url, from_encoding, use_lxml, expected):
    with patch('requests.get') as mock_get:
        if url == "http://example.com":
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = b"<html><body></body></html>"
            mock_get.return_value = mock_response
        elif url == "":
            mock_get.return_value = None
        else:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

        result = task_func(url, from_encoding, use_lxml)
        assert isinstance(result, BeautifulSoup) if expected else result is None

@pytest.mark.parametrize("use_lxml, parser", [
    (False, "html.parser"),
    (True, "lxml"),
])
def test_parser_selection(use_lxml, parser):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body></body></html>"
        mock_get.return_value = mock_response

        result = task_func(URL, use_lxml=use_lxml)
        assert result.prettify().startswith(f"<html><head></head><body></body></html>")  # Check basic structure
        assert result.builder.parser == parser  # Check parser used

def test_exception_handling():
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body></body></html>"
        mock_get.side_effect = Exception("Simulated error")

        result = task_func(URL)
        assert result is None