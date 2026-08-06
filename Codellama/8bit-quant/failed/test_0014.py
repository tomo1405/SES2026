import pytest
from src_0014 import task_func

def test_task_func():
    # Test that the function can connect to the FTP server
    ftp_server = 'ftp.dlptest.com'
    ftp_user = 'dlpuser'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_dir = '/ftp/test'
    downloaded_files = task_func(ftp_server, ftp_user, ftp_password, ftp_dir)
    assert downloaded_files == ['file1.txt', 'file2.txt', 'file3.txt']

def test_task_func_invalid_ftp_server():
    # Test that the function raises an exception if the FTP server is invalid
    ftp_server = 'invalid_ftp_server'
    ftp_user = 'dlpuser'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_dir = '/ftp/test'
    with pytest.raises(Exception) as e:
        task_func(ftp_server, ftp_user, ftp_password, ftp_dir)
    assert str(e.value) == f'Failed to connect to FTP server {ftp_server}: [Errno 11001] getaddrinfo failed'

def test_task_func_invalid_ftp_user():
    # Test that the function raises an exception if the FTP user is invalid
    ftp_server = 'ftp.dlptest.com'
    ftp_user = 'invalid_ftp_user'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_dir = '/ftp/test'
    with pytest.raises(Exception) as e:
        task_func(ftp_server, ftp_user, ftp_password, ftp_dir)
    assert str(e.value) == f'Failed to log into FTP server {ftp_server} with user {ftp_user}: [Errno 530] Login incorrect.'

def test_task_func_invalid_ftp_dir():
    # Test that the function raises an exception if the FTP directory is invalid
    ftp_server = 'ftp.dlptest.com'
    ftp_user = 'dlpuser'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_dir = '/invalid/ftp/dir'
    with pytest.raises(Exception) as e:
        task_func(ftp_server, ftp_user, ftp_password, ftp_dir)
    assert str(e.value) == f'Failed to change to directory {ftp_dir} on server {ftp_server}: [Errno 550] File not found.'