import pytest
from src_0014 import task_func

def test_task_func_default_parameters():
    with pytest.raises(Exception) as excinfo:
        task_func()
    assert 'Failed to connect to FTP server ftp.dlptest.com' in str(excinfo.value)

def test_task_func_custom_parameters():
    with pytest.raises(Exception) as excinfo:
        task_func(ftp_server='invalid_server', ftp_user='invalid_user', ftp_password='invalid_password')
    assert 'Failed to connect to FTP server invalid_server' in str(excinfo.value)

def test_task_func_directory_not_exist():
    with pytest.raises(Exception) as excinfo:
        task_func(ftp_dir='/non_existent_dir')
    assert 'Failed to change to directory /non_existent_dir' in str(excinfo.value)

def test_task_func_download_files(mocker):
    mock_subprocess_call = mocker.patch('subprocess.call')
    mock_ftp_obj = mocker.Mock(spec=ftplib.FTP)
    mock_ftp_obj.nlst.return_value = ['file1.txt', 'file2.txt']
    
    def mock_login(user, password):
        if user == 'dlpuser' and password == 'rNrKYTX9g7z3RgJRmxWuGHbeu':
            return True
        else:
            raise ftplib.error_perm('530 Login authentication failed')

    mock_ftp_obj.login = mock_login

    def mock_cwd(directory):
        if directory == '/ftp/test':
            return True
        else:
            raise ftplib.error_perm('550 Failed to change directory')

    mock_ftp_obj.cwd = mock_cwd

    with pytest.raises(Exception) as excinfo:
        task_func()
    assert 'Failed to log into FTP server ftp.dlptest.com with user dlpuser' in str(excinfo.value)

    mock_subprocess_call.assert_called_with('wget ftp://dlpuser:rNrKYTX9g7z3RgJRmxWuGHbeu@ftp.dlptest.com/ftp/test/file1.txt -P downloaded_files', shell=True)
    mock_subprocess_call.assert_called_with('wget ftp://dlpuser:rNrKYTX9g7z3RgJRmxWuGHbeu@ftp.dlptest.com/ftp/test/file2.txt -P downloaded_files', shell=True)