import pytest
from src_0995 import task_func
from unittest.mock import patch, MagicMock
import pandas as pd

@patch('src_0995.requests.get')
@patch('src_0995.BeautifulSoup')
def test_task_func(mock_bs, mock_requests_get):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
    <body>
        <div class="container">
            <h1>Title 1</h1>
            <span class="date">Date 1</span>
            <span class="author">Author 1</span>
        </div>
        <div class="container">
            <h1>Title 2</h1>
            <span class="date">Date 2</span>
            <span class="author">Author 2</span>
        </div>
    </body>
    </html>
    """
    mock_requests_get.return_value = mock_response

    # Mock BeautifulSoup
    mock_soup = MagicMock()
    mock_divs = [
        MagicMock(),
        MagicMock()
    ]
    mock_divs[0].find.return_value = MagicMock(text="Title 1")
    mock_divs[0].find_next_sibling.return_value = MagicMock(text="Date 1")
    mock_divs[0].find_next_sibling.return_value.find_next_sibling.return_value = MagicMock(text="Author 1")
    mock_divs[1].find.return_value = MagicMock(text="Title 2")
    mock_divs[1].find_next_sibling.return_value = MagicMock(text="Date 2")
    mock_divs[1].find_next_sibling.return_value.find_next_sibling.return_value = MagicMock(text="Author 2")
    mock_soup.find_all.return_value = mock_divs
    mock_bs.return_value = mock_soup

    # Define the test parameters
    url = "http://example.com"
    csv_file_path = "test.csv"

    # Call the function
    result = task_func(url, csv_file_path)

    # Assert the result
    expected_result = [("Title 1", "Date 1", "Author 1"), ("Title 2", "Date 2", "Author 2")]
    assert result == expected_result

    # Check if DataFrame was created and saved correctly
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(expected_result, columns=["Title", "Date", "Author"]))

    # Clean up the test file
    import os
    os.remove(csv_file_path)

@patch('src_0995.requests.get')
def test_task_func_request_exception(mock_requests_get):
    # Mock the request to raise an exception
    mock_requests_get.side_effect = requests.RequestException("Network error")

    # Define the test parameters
    url = "http://example.com"
    csv_file_path = "test.csv"

    # Assert that a RuntimeError is raised
    with pytest.raises(RuntimeError, match="Error fetching URL: Network error"):
        task_func(url, csv_file_path)

@patch('src_0995.BeautifulSoup')
def test_task_func_missing_elements(mock_bs):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <html>
    <body>
        <div class="container">
            <h1>Title 1</h1>
        </div>
    </body>
    </html>
    """
    mock_requests_get.return_value = mock_response

    # Mock BeautifulSoup
    mock_soup = MagicMock()
    mock_divs = [MagicMock()]
    mock_divs[0].find.return_value = MagicMock(text="Title 1")
    mock_divs[0].find_next_sibling.return_value = None
    mock_divs[0].find_next_sibling.return_value.find_next_sibling.return_value = None
    mock_soup.find_all.return_value = mock_divs
    mock_bs.return_value = mock_soup

    # Define the test parameters
    url = "http://example.com"
    csv_file_path = "test.csv"

    # Call the function
    result = task_func(url, csv_file_path)

    # Assert the result
    expected_result = [("Title 1", "No Date", "No Author")]
    assert result == expected_result

    # Check if DataFrame was created and saved correctly
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(expected_result, columns=["Title", "Date", "Author"]))

    # Clean up the test file
    import os
    os.remove(csv_file_path)