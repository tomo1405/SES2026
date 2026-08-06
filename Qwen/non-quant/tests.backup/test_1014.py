import pytest
from unittest.mock import patch, MagicMock
from src_1014 import task_func
import csv
from io import StringIO

@pytest.fixture
def mock_response():
    response = MagicMock()
    response.status_code = 200
    response.text = "<html><body><a href='/page1'>Page 1</a><a href='/page2'>Page 2</a></body></html>"
    return response

@patch('src_1014.requests.get')
def test_task_func(mock_get, mock_response):
    mock_get.return_value = mock_response
    base_url = "https://www.example.com"
    url = "/test"
    csv_file = StringIO()

    result = task_func(url, base_url, csv_file)

    assert result == 2

    expected_links = [
        ['https://www.example.com/page1'],
        ['https://www.example.com/page2']
    ]

    csv_file.seek(0)
    reader = csv.reader(csv_file)
    actual_links = [row for row in reader]

    assert actual_links == expected_links

@patch('src_1014.requests.get')
def test_task_func_no_links(mock_get, mock_response):
    mock_response.text = "<html><body>No links here</body></html>"
    mock_get.return_value = mock_response
    base_url = "https://www.example.com"
    url = "/test"
    csv_file = StringIO()

    result = task_func(url, base_url, csv_file)

    assert result == 0

    csv_file.seek(0)
    reader = csv.reader(csv_file)
    actual_links = [row for row in reader]

    assert actual_links == []

@patch('src_1014.requests.get')
def test_task_func_relative_base_url(mock_get, mock_response):
    mock_get.return_value = mock_response
    base_url = "/relative"
    url = "/test"
    csv_file = StringIO()

    result = task_func(url, base_url, csv_file)

    assert result == 2

    expected_links = [
        ['/relative/page1'],
        ['/relative/page2']
    ]

    csv_file.seek(0)
    reader = csv.reader(csv_file)
    actual_links = [row for row in reader]

    assert actual_links == expected_links

@patch('src_1014.requests.get')
def test_task_func_http_error(mock_get):
    mock_get.return_value.status_code = 404
    base_url = "https://www.example.com"
    url = "/test"
    csv_file = StringIO()

    with pytest.raises(requests.exceptions.HTTPError):
        task_func(url, base_url, csv_file)