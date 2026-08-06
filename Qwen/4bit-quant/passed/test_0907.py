import pytest
from src_0907 import task_func
import os
import zipfile

def test_task_func(tmpdir):
    source_dir = tmpdir.mkdir('source')
    target_dir = tmpdir.mkdir('target')

    # Create some files in the source directory
    processed_file = source_dir.join('file_processed.txt')
    processed_file.write('This is a processed file.')
    unprocessed_file = source_dir.join('file_unprocessed.txt')
    unprocessed_file.write('This is an unprocessed file.')

    archive_name = 'test_archive.zip'
    archive_path = task_func(str(source_dir), str(target_dir), archive_name)

    # Check if the archive was created
    assert os.path.exists(archive_path)

    # Check if the archive contains the processed file
    with zipfile.ZipFile(archive_path, 'r') as archive:
        assert 'file_processed.txt' in archive.namelist()

    # Check if the processed file was moved to the target directory
    assert os.path.exists(os.path.join(target_dir, 'file_processed.txt'))

    # Check if the unprocessed file is still in the source directory
    assert os.path.exists(os.path.join(source_dir, 'file_unprocessed.txt'))

def test_task_func_no_processed_files(tmpdir):
    source_dir = tmpdir.mkdir('source')
    target_dir = tmpdir.mkdir('target')

    archive_name = 'test_archive.zip'
    archive_path = task_func(str(source_dir), str(target_dir), archive_name)

    # Check if the archive was created
    assert os.path.exists(archive_path)

    # Check if the archive is empty
    with zipfile.ZipFile(archive_path, 'r') as archive:
        assert len(archive.namelist()) == 0

def test_task_func_empty_source_dir(tmpdir):
    source_dir = tmpdir.mkdir('source')
    target_dir = tmpdir.mkdir('target')

    archive_name = 'test_archive.zip'
    archive_path = task_func(str(source_dir), str(target_dir), archive_name)

    # Check if the archive was created
    assert os.path.exists(archive_path)

    # Check if the archive is empty
    with zipfile.ZipFile(archive_path, 'r') as archive:
        assert len(archive.namelist()) == 0