import pytest
from src_0014 import task_func

def test_task_func():
    with pytest.raises(Exception) as exc_info:
        task_func(ftp_server='not_a_valid_server', ftp_user='user', ftp_password='password', ftp_dir='/dir')
    assert 'Failed to connect to FTP server' in str(exc_info.value)

    with pytest.raises(Exception) as exc_info:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='not_a_valid_user', ftp_password='password', ftp_dir='/dir')
    assert 'Failed to log into FTP server' in str(exc_info.value)

    with pytest.raises(Exception) as exc_info:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='user', ftp_password='not_a_valid_password', ftp_dir='/dir')
    assert 'Failed to log into FTP server' in str(exc_info.value)

    with pytest.raises(Exception) as exc_info:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='user', ftp_password='password', ftp_dir='not_a_valid_dir')
    assert 'Failed to change to directory' in str(exc_info.value)

    downloaded_files = task_func()
    assert len(downloaded_files) > 0
    for filename in downloaded_files:
        assert os.path.exists(f"downloaded_files/{filename}")