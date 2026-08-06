import pytest
from src_0014 import task_func

def test_task_func():
    # Test case 1: Valid FTP connection and file download
    downloaded_files = task_func()
    assert len(downloaded_files) > 0
    for filename in downloaded_files:
        assert os.path.exists(f"downloaded_files/{filename}")

    # Test case 2: Invalid FTP server
    with pytest.raises(Exception) as exc_info:
        task_func(ftp_server='invalid_server')
    assert "Failed to connect to FTP server" in str(exc_info.value)

    # Test case 3: Invalid FTP credentials
    with pytest.raises(Exception) as exc_info:
        task_func(ftp_user='invalid_user', ftp_password='invalid_password')
    assert "Failed to log into FTP server" in str(exc_info.value)

    # Test case 4: Invalid directory path
    with pytest.raises(Exception) as exc_info:
        task_func(ftp_dir='/invalid_directory')
    assert "Failed to change to directory" in str(exc_info.value)