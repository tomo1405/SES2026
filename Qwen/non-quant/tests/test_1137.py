import pytest
from src_1137 import task_func
import os
import re

@pytest.fixture
def mock_requests_get(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><p>test@example.com</p></body></html>"
    mocker.patch('requests.get', return_value=mock_response)

def test_task_func(mock_requests_get, tmpdir):
    csv_path = str(tmpdir / "emails.csv")
    result = task_func(url="http://example.com", csv_path=csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows[0] == ['Emails']
    assert rows[1] == ['test@example.com']

def test_task_func_no_emails(mock_requests_get, tmpdir):
    csv_path = str(tmpdir / "emails.csv")
    mock_response = mock_requests_get.return_value
    mock_response.text = "<html><body><p>No emails here</p></body></html>"
    
    result = task_func(url="http://example.com", csv_path=csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    assert rows[0] == ['Emails']
    assert len(rows) == 1

def test_task_func_invalid_url(mock_requests_get, tmpdir):
    csv_path = str(tmpdir / "emails.csv")
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 404
    
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url="http://invalid-url.com", csv_path=csv_path)