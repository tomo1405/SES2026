import pytest
from src_0014 import task_func
import os
import shutil
import ftplib
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_ftp_mock():
    with patch('ftplib.FTP') as mock_ftp:
        yield mock_ftp

@pytest.fixture
def setup_subprocess_mock():
    with patch('subprocess.call') as mock_call:
        yield mock_call

@pytest.fixture
def cleanup_downloaded_files():
    download_dir = "downloaded_files"
    yield
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

def test_task_func_success(setup_ftp_mock, setup_subprocess_mock, cleanup_downloaded_files):
    mock_ftp = setup_ftp_mock.return_value
    mock_ftp.nlst.return_value = ['file1.txt', 'file2.txt']
    
    result = task_func()

    assert result == ['file1.txt', 'file2.txt']
    mock_ftp.connect.assert_called_once_with('ftp.dlptest.com')
    mock_ftp.login.assert_called_once_with('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
    mock_ftp.cwd.assert_called_once_with('/ftp/test')
    setup_subprocess_mock.assert_has_calls([
        pytest.call(f'wget ftp://dlpuser:rNrKYTX9g7z3RgJRmxWuGHbeu@ftp.dlptest.com/ftp/test/file1.txt -P downloaded_files', shell=True),
        pytest.call(f'wget ftp://dlpuser:rNrKYTX9g7z3RgJRmxWuGHbeu@ftp.dlptest.com/ftp/test/file2.txt -P downloaded_files', shell=True)
    ])
    mock_ftp.quit.assert_called_once()

def test_task_func_connection_failure(setup_ftp_mock):
    mock_ftp = setup_ftp_mock.return_value
    mock_ftp.connect.side_effect = Exception("Connection failed")

    with pytest.raises(Exception) as exc_info:
        task_func()

    assert str(exc_info.value) == 'Failed to connect to FTP server ftp.dlptest.com: Connection failed'

def test_task_func_login_failure(setup_ftp_mock):
    mock_ftp = setup_ftp_mock.return_value
    mock_ftp.login.side_effect = Exception("Login failed")

    with pytest.raises(Exception) as exc_info:
        task_func()

    assert str(exc_info.value) == 'Failed to log into FTP server ftp.dlptest.com with user dlpuser: Login failed'

def test_task_func_directory_change_failure(setup_ftp_mock):
    mock_ftp = setup_ftp_mock.return_value
    mock_ftp.cwd.side_effect = Exception("Directory change failed")

    with pytest.raises(Exception) as exc_info:
        task_func()

    assert str(exc_info.value) == 'Failed to change to directory /ftp/test on server ftp.dlptest.com: Directory change failed'