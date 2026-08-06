import pytest
from src_0813 import task_func
import os
import tarfile
from pathlib import Path

@pytest.fixture
def temp_dir(tmpdir):
    """Create a temporary directory with some files."""
    temp_dir = Path(tmpdir)
    (temp_dir / "AcroTray.exe").touch()
    (temp_dir / "SubDir" / "AcroTray.exe").touch()
    (temp_dir / "SubDir" / "OtherFile.txt").touch()
    return temp_dir

def test_task_func(temp_dir):
    # Define a pattern to match AcroTray.exe
    pattern = r"(?<!Distillr)\\\\AcroTray\.exe"
    
    # Call the function with the temporary directory and pattern
    archive_path = task_func(str(temp_dir), pattern)
    
    # Check if the archive file exists
    assert Path(archive_path).exists()
    
    # Extract the tar file and check its contents
    with tarfile.open(archive_path, 'r') as tar:
        members = tar.getnames()
        assert len(members) == 2
        assert "AcroTray.exe" in members
        assert "SubDir/AcroTray.exe" in members

def test_task_func_permission_error(monkeypatch, capsys, temp_dir):
    # Define a pattern to match AcroTray.exe
    pattern = r"(?<!Distillr)\\\\AcroTray\.exe"
    
    # Mock a permission error when adding a file to the tar
    def mock_add(self, path, arcname=None):
        raise PermissionError("Permission denied")
    
    monkeypatch.setattr(tarfile.TarFile, 'add', mock_add)
    
    # Call the function with the temporary directory and pattern
    archive_path = task_func(str(temp_dir), pattern)
    
    # Check if the archive file exists
    assert Path(archive_path).exists()
    
    # Capture the output and check if the permission error message is printed
    captured = capsys.readouterr()
    assert "Skipping AcroTray.exe due to permission error: Permission denied" in captured.out
    assert "Skipping SubDir/AcroTray.exe due to permission error: Permission denied" in captured.out