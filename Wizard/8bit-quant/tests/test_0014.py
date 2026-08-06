python
import subprocess
import ftplib
import os
import pytest

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    # Attempt to connect to the FTP server
    try:
        ftp_obj = ftplib.FTP(ftp_server)
    except Exception as e:
        raise Exception(f'Failed to connect to FTP server {ftp_server}: {str(e)}')

    # Attempt to login to the FTP server
    try:
        ftp_obj.login(ftp_user, ftp_password)
    except Exception as e:
        raise Exception(f'Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}')

    # Attempt to change to the specified directory
    try:
        ftp_obj.cwd(ftp_dir)
    except Exception as e:
        raise Exception(f'Failed to change to directory {ftp_dir} on server {ftp_server}: {str(e)}')

    # Directory to store downloaded files
    download_dir = "downloaded_files"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    downloaded_files = []
    for filename in ftp_obj.nlst():
        command = f'wget ftp://{ftp_user}:{ftp_password}@{ftp_server}{ftp_dir}/{filename} -P {download_dir}'
        subprocess.call(command, shell=True)
        downloaded_files.append(filename)

    ftp_obj.quit()
    return downloaded_files

def test_task_func():
    # Test case 1: Valid input
    downloaded_files = task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test')
    assert len(downloaded_files) > 0

    # Test case 2: Invalid FTP server
    with pytest.raises(Exception) as e:
        task_func(ftp_server='ftp.invalidserver.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test')
    assert str(e.value) == 'Failed to connect to FTP server ftp.invalidserver.com: [Errno 11001] getaddrinfo failed'

    # Test case 3: Invalid FTP user
    with pytest.raises(Exception) as e:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='invaliduser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test')
    assert str(e.value) == 'Failed to log into FTP server ftp.dlptest.com with user invaliduser: [Errno 11001] getaddrinfo failed'

    # Test case 4: Invalid FTP password
    with pytest.raises(Exception) as e:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='invalidpassword', ftp_dir='/ftp/test')
    assert str(e.value) == 'Failed to log into FTP server ftp.dlptest.com with user dlpuser: [Errno 11001] getaddrinfo failed'

    # Test case 5: Invalid FTP directory
    with pytest.raises(Exception) as e:
        task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/invalid/directory')
    assert str(e.value) == 'Failed to change to directory /invalid/directory on server ftp.dlptest.com: [Errno 11001] getaddrinfo failed'