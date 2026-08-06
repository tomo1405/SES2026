import pytest
from src_0998 import task_func
import os
import zipfile

# Mocking urllib.request.urlretrieve and zipfile.ZipFile
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_urlretrieve():
    with patch('src_0998.urllib.request.urlretrieve') as mock:
        yield mock

@pytest.fixture
def mock_zipfile():
    with patch('src_0998.zipfile.ZipFile') as mock:
        yield mock

def test_task_func(mock_urlretrieve, mock_zipfile, tmpdir):
    # Setup
    url = "http://example.com/file.zip"
    expected_dir = str(tmpdir / "downloaded_files")
    os.chdir(str(tmpdir))

    # Mocking behavior
    mock_urlretrieve.return_value = None
    mock_zipfile_instance = MagicMock()
    mock_zipfile.return_value = mock_zipfile_instance
    mock_zipfile_instance.extractall.return_value = None

    # Execute
    result = task_func(url)

    # Assert
    assert result == expected_dir
    mock_urlretrieve.assert_called_once_with(url, "downloaded_files.zip")
    mock_zipfile.assert_called_once_with("downloaded_files.zip", "r")
    mock_zipfile_instance.extractall.assert_called_once_with(expected_dir)
    assert not os.path.exists("downloaded_files.zip")

def test_task_func_directory_creation(mock_urlretrieve, mock_zipfile, tmpdir):
    # Setup
    url = "http://example.com/file.zip"
    expected_dir = str(tmpdir / "downloaded_files")
    os.chdir(str(tmpdir))
    os.rmdir(expected_dir)  # Ensure the directory does not exist initially

    # Mocking behavior
    mock_urlretrieve.return_value = None
    mock_zipfile_instance = MagicMock()
    mock_zipfile.return_value = mock_zipfile_instance
    mock_zipfile_instance.extractall.return_value = None

    # Execute
    result = task_func(url)

    # Assert
    assert os.path.isdir(expected_dir)
    assert result == expected_dir

def test_task_func_file_removal(mock_urlretrieve, mock_zipfile, tmpdir):
    # Setup
    url = "http://example.com/file.zip"
    os.chdir(str(tmpdir))
    open("downloaded_files.zip", "w").close()  # Create the zip file manually

    # Mocking behavior
    mock_urlretrieve.return_value = None
    mock_zipfile_instance = MagicMock()
    mock_zipfile.return_value = mock_zipfile_instance
    mock_zipfile_instance.extractall.return_value = None

    # Execute
    task_func(url)

    # Assert
    assert not os.path.exists("downloaded_files.zip")

def test_task_func_no_zip_file(mock_urlretrieve, mock_zipfile, tmpdir):
    # Setup
    url = "http://example.com/file.zip"
    os.chdir(str(tmpdir))

    # Mocking behavior
    mock_urlretrieve.return_value = None
    mock_zipfile.side_effect = zipfile.BadZipFile

    # Execute & Assert
    with pytest.raises(zipfile.BadZipFile):
        task_func(url)

    # Cleanup
    if os.path.exists("downloaded_files.zip"):
        os.remove("downloaded_files.zip")