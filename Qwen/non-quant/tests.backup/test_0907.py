import pytest
from src_0907 import task_func
import os
import zipfile
import tempfile

def test_task_func():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some test files in the source directory
        test_files = ['file1_processed.txt', 'file2.txt', 'file3_processed.csv']
        for file in test_files:
            with open(os.path.join(source_dir, file), 'w') as f:
                f.write('test content')
        
        # Call the function
        archive_path = task_func(source_dir, target_dir)
        
        # Check if the archive was created
        assert os.path.exists(archive_path)
        
        # Check if the archive contains the correct files
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive_contents = archive.namelist()
            assert 'file1_processed.txt' in archive_contents
            assert 'file3_processed.csv' in archive_contents
            assert 'file2.txt' not in archive_contents
        
        # Check if the processed files were moved to the target directory
        target_files = os.listdir(target_dir)
        assert 'file1_processed.txt' in target_files
        assert 'file3_processed.csv' in target_files
        assert 'file2.txt' not in target_files

def test_task_func_no_processed_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some test files in the source directory without '_processed' suffix
        test_files = ['file1.txt', 'file2.csv']
        for file in test_files:
            with open(os.path.join(source_dir, file), 'w') as f:
                f.write('test content')
        
        # Call the function
        archive_path = task_func(source_dir, target_dir)
        
        # Check if the archive was created
        assert os.path.exists(archive_path)
        
        # Check if the archive is empty
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive_contents = archive.namelist()
            assert not archive_contents
        
        # Check if no files were moved to the target directory
        target_files = os.listdir(target_dir)
        assert not target_files

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Call the function with an empty source directory
        archive_path = task_func(source_dir, target_dir)
        
        # Check if the archive was created
        assert os.path.exists(archive_path)
        
        # Check if the archive is empty
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive_contents = archive.namelist()
            assert not archive_contents
        
        # Check if no files were moved to the target directory
        target_files = os.listdir(target_dir)
        assert not target_files