python
import re
from pathlib import Path
import tarfile
import pytest

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    tar_path = Path(directory) / 'archive.tar'
    with tarfile.open(tar_path, 'w') as tar:
        for path in Path(directory).rglob('*'):
            if re.match(file_pattern, path.name):
                try:
                    tar.add(path, arcname=path.relative_to(directory))
                except PermissionError as e:
                    print(f"Skipping {path} due to permission error: {e}")
    return str(tar_path)

def test_task_func():
    # Test case 1: Default values
    assert task_func() == "C:\\SomeDir\\archive.tar"

    # Test case 2: Custom directory and file pattern
    assert task_func(directory="D:\\SomeOtherDir\\", file_pattern=r"Acrobat.exe") == "D:\\SomeOtherDir\\archive.tar"

    # Test case 3: Invalid directory
    with pytest.raises(FileNotFoundError):
        task_func(directory="E:\\SomeNonexistentDir\\")

    # Test case 4: Invalid file pattern
    with pytest.raises(re.error):
        task_func(file_pattern=r"Acrobat[exe")

    # Test case 5: Permission error
    with pytest.raises(PermissionError):
        task_func(directory="C:\\Windows\\")