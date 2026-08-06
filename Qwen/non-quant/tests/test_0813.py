import pytest
from src_0813 import task_func
from pathlib import Path
import tarfile
import os

# Mocking utilities
from unittest.mock import patch, mock_open

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

@pytest.fixture
def setup_directory(tmpdir):
    # Create a temporary directory structure
    tmpdir.mkdir("SomeDir")
    sub_dir = tmpdir.mkdir("SomeDir").mkdir("subdir")
    sub_dir.join("AcroTray.exe").write("")
    sub_dir.join("DistillrAcroTray.exe").write("")
    sub_dir.join("otherfile.txt").write("")
    return tmpdir

@patch('src_0813.tarfile.open')
@patch('src_0813.Path.rglob')
def test_task_func(mock_rglob, mock_tarfile, setup_directory):
    # Setup
    directory = str(setup_directory.join("SomeDir"))
    mock_rglob.return_value = [
        Path(directory) / "subdir" / "AcroTray.exe",
        Path(directory) / "subdir" / "DistillrAcroTray.exe",
        Path(directory) / "subdir" / "otherfile.txt"
    ]
    
    mock_tar = mock_tarfile.return_value.__enter__.return_value
    
    # Execute
    result = task_func(directory=directory)
    
    # Assert
    assert result == str(Path(directory) / 'archive.tar')
    mock_tar.add.assert_called_once_with(
        Path(directory) / "subdir" / "AcroTray.exe",
        arcname="subdir/AcroTray.exe"
    )

@patch('src_0813.tarfile.open')
@patch('src_0813.Path.rglob')
def test_task_func_permission_error(mock_rglob, mock_tarfile, setup_directory, capsys):
    # Setup
    directory = str(setup_directory.join("SomeDir"))
    mock_rglob.return_value = [
        Path(directory) / "subdir" / "AcroTray.exe"
    ]
    
    mock_tar = mock_tarfile.return_value.__enter__.return_value
    mock_tar.add.side_effect = PermissionError("Permission denied")
    
    # Execute
    result = task_func(directory=directory)
    
    # Assert
    captured = capsys.readouterr()
    assert "Skipping" in captured.out
    assert result == str(Path(directory) / 'archive.tar')

@patch('src_0813.tarfile.open')
@patch('src_0813.Path.rglob')
def test_task_func_no_matching_files(mock_rglob, mock_tarfile, setup_directory):
    # Setup
    directory = str(setup_directory.join("SomeDir"))
    mock_rglob.return_value = []
    
    # Execute
    result = task_func(directory=directory)
    
    # Assert
    mock_tarfile.return_value.__enter__.assert_not_called()
    assert result == str(Path(directory) / 'archive.tar')