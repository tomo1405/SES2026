import pytest
from src_0316 import task_func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
import os
import tempfile

def test_task_func_directory_not_exists():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_dir', 'fake_api_key', 'test@example.com')
    assert str(excinfo.value) == "Directory 'non_existent_dir' does not exist."

def test_task_func_sendgrid_success(mocker):
    mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    mocker.patch.object(SendGridAPIClient, 'send', return_value=mocker.Mock(status_code=200))
    
    result = task_func(tempfile.gettempdir(), 'fake_api_key', 'test@example.com')
    assert result is True

def test_task_func_sendgrid_http_error(mocker):
    mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    mocker.patch.object(SendGridAPIClient, 'send', side_effect=HTTPError("HTTP Error"))
    
    with pytest.raises(HTTPError) as excinfo:
        task_func(tempfile.gettempdir(), 'fake_api_key', 'test@example.com')
    assert str(excinfo.value) == "HTTP Error"

def test_task_func_other_exception(mocker):
    mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    mocker.patch.object(SendGridAPIClient, 'send', side_effect=Exception("General Error"))
    
    with pytest.raises(Exception) as excinfo:
        task_func(tempfile.gettempdir(), 'fake_api_key', 'test@example.com')
    assert str(excinfo.value) == "General Error"