import csv
import os
import re

import pytest
import requests
from src_1137 import task_func


@pytest.fixture
def mock_requests_get(monkeypatch):
    class MockResponse:
        def __init__(self, text):
            self.text = text

    def mock_get(*args, **kwargs):
        return MockResponse("<html><body><p>test@example.com</p></body></html>")

    monkeypatch.setattr(requests, 'get', mock_get)

def test_task_func(mock_requests_get, tmpdir):
    # Create a temporary directory and set the CSV path within it
    csv_path = str(tmpdir.join('emails.csv'))
    
    # Call the function with the temporary CSV path
    result = task_func(csv_path=csv_path)
    
    # Assert that the result is the correct CSV path
    assert result == csv_path
    
    # Check if the CSV file was created
    assert os.path.exists(csv_path)
    
    # Read the CSV file and check its contents
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # The first row should be the header
    assert rows[0] == ['Emails']
    
    # The second row should contain the email address
    assert len(rows) == 2
    assert re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", rows[1][0])

def test_task_func_no_emails(mock_requests_get, tmpdir):
    # Create a temporary directory and set the CSV path within it
    csv_path = str(tmpdir.join('emails.csv'))
    
    # Call the function with the temporary CSV path
    result = task_func(csv_path=csv_path)
    
    # Assert that the result is the correct CSV path
    assert result == csv_path
    
    # Check if the CSV file was created
    assert os.path.exists(csv_path)
    
    # Read the CSV file and check its contents
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # The first row should be the header
    assert rows[0] == ['Emails']
    
    # There should be no additional rows with email addresses
    assert len(rows) == 1