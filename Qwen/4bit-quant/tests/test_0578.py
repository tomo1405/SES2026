import pytest
from src_0578 import task_func
import os
import pathlib
from hashlib import md5
import unicodedata

# Mocking utilities
from unittest.mock import patch, mock_open

def test_task_func_with_empty_directory(tmp_path):
    # Create an empty directory
    empty_dir = tmp_path / "empty_dir"
    empty_dir.mkdir()

    result = task_func(str(empty_dir))
    assert result == {}

def test_task_func_with_single_file(tmp_path):
    # Create a directory with a single file
    single_file_dir = tmp_path / "single_file_dir"
    single_file_dir.mkdir()

    file_path = single_file_dir / "test_file.txt"
    file_content = b"Hello, World!"
    with open(file_path, 'wb') as file:
        file.write(file_content)

    expected_normalized_name = unicodedata.normalize('NFKD', file_path.name).encode('ascii', 'ignore').decode()
    expected_hash = md5(file_content).hexdigest()
    expected_result = {
        expected_normalized_name: {
            'Size': len(file_content),
            'MD5 Hash': expected_hash
        }
    }

    result = task_func(str(single_file_dir))
    assert result == expected_result

def test_task_func_with_multiple_files(tmp_path):
    # Create a directory with multiple files
    multiple_files_dir = tmp_path / "multiple_files_dir"
    multiple_files_dir.mkdir()

    files = [
        ("file1.txt", b"Content of file 1"),
        ("file2.txt", b"Content of file 2"),
        ("file3.txt", b"Content of file 3")
    ]

    for file_name, content in files:
        file_path = multiple_files_dir / file_name
        with open(file_path, 'wb') as file:
            file.write(content)

    expected_result = {}
    for file_name, content in files:
        normalized_name = unicodedata.normalize('NFKD', file_name).encode('ascii', 'ignore').decode()
        file_hash = md5(content).hexdigest()
        expected_result[normalized_name] = {
            'Size': len(content),
            'MD5 Hash': file_hash
        }

    result = task_func(str(multiple_files_dir))
    assert result == expected_result

@patch('src_0578.os.path.getsize')
@patch('src_0578.open', new_callable=mock_open)
def test_task_func_with_non_ascii_filename(mock_open, mock_getsize, tmp_path):
    # Create a directory with a file having non-ASCII characters in its name
    non_ascii_dir = tmp_path / "non_ascii_dir"
    non_ascii_dir.mkdir()

    file_path = non_ascii_dir / "café.txt"
    file_content = b"Content with café"
    with open(file_path, 'wb') as file:
        file.write(file_content)

    expected_normalized_name = unicodedata.normalize('NFKD', file_path.name).encode('ascii', 'ignore').decode()
    expected_hash = md5(file_content).hexdigest()

    mock_getsize.return_value = len(file_content)
    mock_open.return_value.read.return_value = file_content

    expected_result = {
        expected_normalized_name: {
            'Size': len(file_content),
            'MD5 Hash': expected_hash
        }
    }

    result = task_func(str(non_ascii_dir))
    assert result == expected_result

def test_task_func_with_subdirectories(tmp_path):
    # Create a directory with subdirectories and files
    root_dir = tmp_path / "root_dir"
    root_dir.mkdir()

    sub_dir = root_dir / "sub_dir"
    sub_dir.mkdir()

    files = [
        (root_dir / "file1.txt", b"Root file content"),
        (sub_dir / "file2.txt", b"Subdirectory file content")
    ]

    for file_path, content in files:
        with open(file_path, 'wb') as file:
            file.write(content)

    expected_normalized_name_root = unicodedata.normalize('NFKD', files[0][0].name).encode('ascii', 'ignore').decode()
    expected_hash_root = md5(files[0][1]).hexdigest()

    expected_normalized_name_sub = unicodedata.normalize('NFKD', files[1][0].name).encode('ascii', 'ignore').decode()
    expected_hash_sub = md5(files[1][1]).hexdigest()

    expected_result = {
        expected_normalized_name_root: {
            'Size': len(files[0][1]),
            'MD5 Hash': expected_hash_root
        },
        expected_normalized_name_sub: {
            'Size': len(files[1][1]),
            'MD5 Hash': expected_hash_sub
        }
    }

    result = task_func(str(root_dir))
    assert result == expected_result