import pytest
from src_0014 import task_func

def test_task_func():
    # Test that the function returns a list of downloaded files
    downloaded_files = task_func()
    assert isinstance(downloaded_files, list)

    # Test that the function raises an exception if it fails to connect to the FTP server
    with pytest.raises(Exception):
        task_func(ftp_server='invalid_server')

    # Test that the function raises an exception if it fails to log in to the FTP server
    with pytest.raises(Exception):
        task_func(ftp_user='invalid_user')

    # Test that the function raises an exception if it fails to change to the specified directory
    with pytest.raises(Exception):
        task_func(ftp_dir='invalid_dir')

    # Test that the function raises an exception if it fails to download a file
    with pytest.raises(Exception):
        task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test', filename='invalid_file')