python
import subprocess
import ftplib
import os

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
    # Test case 1: Valid FTP credentials
    downloaded_files = task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test')
    assert len(downloaded_files) > 0

    # Test case 2: Invalid FTP credentials
    try:
        downloaded_files = task_func(ftp_server='ftp.dlptest.com', ftp_user='invalid_user', ftp_password='invalid_password', ftp_dir='/ftp/test')
        assert False
    except Exception as e:
        assert str(e) == 'Failed to log into FTP server ftp.dlptest.com with user invalid_user: 530 Login authentication failed.'

    # Test case 3: Invalid FTP directory
    try:
        downloaded_files = task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/invalid_dir')
        assert False
    except Exception as e:
        assert str(e) == 'Failed to change to directory /invalid_dir on server ftp.dlptest.com: 550 Failed to change directory.'

    # Test case 4: Invalid FTP server
    try:
        downloaded_files = task_func(ftp_server='invalid_server', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test')
        assert False
    except Exception as e:
        assert str(e) == 'Failed to connect to FTP server invalid_server: 60-100 Connection timed out.'