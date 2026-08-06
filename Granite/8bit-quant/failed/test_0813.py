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
            MagicMock(name='file1.txt', spec=Path),
            MagicMock(name='file2.txt', spec=Path),
            MagicMock(name='file3.txt', spec=Path)
        ]
        with patch('tarfile.open', mock_open()) as mock_tar:
            mock_tar.return_value.__enter__.return_value = MagicMock(spec=tarfile.TarFile)
            result = task_func()
            mock_tar.assert_called_once_with(str(Path(DIRECTORY) / 'archive.tar'), 'w')
            mock_tar.return_value.__enter__.return_value.add.assert_has_calls([
                call(mock_path.return_value.glob.return_value[0], arcname='file1.txt'),
                call(mock_path.return_value.glob.return_value[1], arcname='file2.txt'),
                call(mock_path.return_value.glob.return_value[2], arcname='file3.txt')
            ])
            assert result == str(Path(DIRECTORY) / 'archive.tar')

def test_task_func_with_permission_error():
    with patch('pathlib.Path') as mock_path:
        mock_path.return_value.glob.return_value = [
            MagicMock(name='file1.txt', spec=Path),
            MagicMock(name='file2.txt', spec=Path),
            MagicMock(name='file3.txt', spec=Path)
        ]
        with patch('tarfile.open', mock_open()) as mock_tar:
            mock_tar.return_value.__enter__.return_value = MagicMock(spec=tarfile.TarFile)
            mock_tar.return_value.__enter__.return_value.add.side_effect = [
                PermissionError('Mock Permission Error'), None, None
            ]
            result = task_func()
            mock_tar.assert_called_once_with(str(Path(DIRECTORY) / 'archive.tar'), 'w')
            mock_tar.return_value.__enter__.return_value.add.assert_has_calls([
                call(mock_path.return_value.glob.return_value[0], arcname='file1.txt'),
                call(mock_path.return_value.glob.return_value[1], arcname='file2.txt'),
                call(mock_path.return_value.glob.return_value[2], arcname='file3.txt')
            ])
            assert result == str(Path(DIRECTORY) / 'archive.tar')