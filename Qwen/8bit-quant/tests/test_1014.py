import csv
import os
from unittest.mock import Mock, patch

import pytest
from bs4 import BeautifulSoup
from src_1014 import task_func


@pytest.mark.parametrize(
    "url, base_url, csv_file, expected_links_count, mock_response_text",
    [
        (
            "/page1",
            "https://www.example.com",
            "test_scraped_data.csv",
            3,
            "<html><body><a href='/link1'>Link 1</a><a href='/link2'>Link 2</a><a href='https://external.com/link3'>Link 3</a></body></html>"
        ),
        (
            "/page2",
            "https://www.example.com",
            "test_scraped_data.csv",
            0,
            "<html><body>No links here</body></html>"
        ),
    ]
)
@patch("requests.get")
def test_task_func(mock_get, url, base_url, csv_file, expected_links_count, mock_response_text):
    # Mock the response from requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = mock_response_text
    mock_get.return_value = mock_response

    # Call the function
    result = task_func(url, base_url, csv_file)

    # Assert the result
    assert result == expected_links_count

    # Assert that the CSV file was written correctly
    with open(csv_file, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        links_in_csv = [row[0] for row in reader]
    
    # Calculate expected links in CSV
    expected_links_in_csv = set(
        urljoin(base_url, a["href"])
        for a in BeautifulSoup(mock_response_text, "html.parser").find_all("a", href=True)
    )

    assert set(links_in_csv) == expected_links_in_csv

    # Clean up the test CSV file
    os.remove(csv_file)