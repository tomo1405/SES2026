import re
from pathlib import Path
import tarfile
from unittest.mock import patch, mock_open, MagicMock

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
    with patch('pathlib.Path') as mock_path:
        mock_path.return_value.glob.return_value = [
            MagicMock(name='file1.txt'),
            MagicMock(name='file2.txt'),
            MagicMock(name='file3.txt')
        ]
        with patch('tarfile.open', mock_open()) as mock_tar:
            mock_tar.return_value.__enter__.return_value = MagicMock()
            result = task_func()
            mock_tar.assert_called_once_with('C:\\SomeDir\\archive.tar', 'w')
            mock_tar.return_value.__enter__.return_value.add.assert_has_calls([
                call('file1.txt', arcname='file1.txt'),
                call('file2.txt', arcname='file2.txt'),
                call('file3.txt', arcname='file3.txt')
            ])
            assert result == 'C:\\SomeDir\\archive.tar'

def test_task_func_with_permission_error():
    with patch('pathlib.Path') as mock_path:
        mock_path.return_value.glob.return_value = [
            MagicMock(name='file1.txt'),
            MagicMock(name='file2.txt'),
            MagicMock(name='file3.txt')
        ]
        with patch('tarfile.open', mock_open()) as mock_tar:
            mock_tar.return_value.__enter__.return_value = MagicMock()
            mock_tar.return_value.__enter__.return_value.add.side_effect = [
                PermissionError('mock error')
            ]
            result = task_func()
            mock_tar.assert_called_once_with('C:\\SomeDir\\archive.tar', 'w')
            mock_tar.return_value.__enter__.return_value.add.assert_has_calls([
                call('file1.txt', arcname='file1.txt'),
                call('file2.txt', arcname='file2.txt'),
                call('file3.txt', arcname='file3.txt')
            ])
            assert result == 'C:\\SomeDir\\archive.tar'
            print.assert_called_once_with('Skipping file1.txt due to permission error: mock error')