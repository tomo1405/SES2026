python
import re
from pathlib import Path
import tarfile
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

# Test cases
def test_task_func_default():
    assert task_func() == 'C:\\SomeDir\\archive.tar'

def test_task_func_custom_directory():
    assert task_func(directory='D:\\') == 'D:\\archive.tar'

def test_task_func_custom_pattern():
    assert task_func(file_pattern=r"AcroTray\.exe") == 'C:\\SomeDir\\archive.tar'

def test_task_func_custom_directory_and_pattern():
    assert task_func(directory='D:\\', file_pattern=r"AcroTray\.exe") == 'D:\\archive.tar'