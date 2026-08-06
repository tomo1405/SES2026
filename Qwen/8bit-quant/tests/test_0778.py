import pytest
from src_0778 import task_func
import os
import zipfile
import tempfile
import shutil

def create_temp_files(temp_dir, filenames):
    for filename in filenames:
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, 'w') as f:
            f.write('test content')

def create_zip_file(temp_dir, base_name, files_to_zip):
    zip_path = os.path.join(temp_dir, f"{base_name}-1.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(os.path.join(temp_dir, file), arcname=file)
    return zip_path

def test_task_func():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files and zip them
        test_files = ['file1.txt', 'file2.txt']
        create_temp_files(temp_dir, test_files)
        zip_file_base = 'test'
        create_zip_file(temp_dir, zip_file_base, test_files)

        # Run the function
        result = task_func(temp_dir)

        # Check if the directory was created and files were extracted
        expected_extracted_dir = os.path.join(temp_dir, zip_file_base)
        assert os.path.exists(expected_extracted_dir)
        for file in test_files:
            assert os.path.exists(os.path.join(expected_extracted_dir, file))

        # Check if the result contains the correct path
        assert result == [expected_extracted_dir]

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files that do not match the pattern
        test_files = ['file1.txt', 'file2.zip']
        create_temp_files(temp_dir, test_files)

        # Run the function
        result = task_func(temp_dir)

        # Check if no directories were created
        assert result == []

def test_task_func_multiple_zips():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple zip files with different base names
        test_files1 = ['file1.txt', 'file2.txt']
        test_files2 = ['file3.txt', 'file4.txt']
        create_temp_files(temp_dir, test_files1 + test_files2)
        zip_file_base1 = 'test1'
        zip_file_base2 = 'test2'
        create_zip_file(temp_dir, zip_file_base1, test_files1)
        create_zip_file(temp_dir, zip_file_base2, test_files2)

        # Run the function
        result = task_func(temp_dir)

        # Check if both directories were created and files were extracted
        expected_extracted_dir1 = os.path.join(temp_dir, zip_file_base1)
        expected_extracted_dir2 = os.path.join(temp_dir, zip_file_base2)
        assert os.path.exists(expected_extracted_dir1)
        assert os.path.exists(expected_extracted_dir2)
        for file in test_files1:
            assert os.path.exists(os.path.join(expected_extracted_dir1, file))
        for file in test_files2:
            assert os.path.exists(os.path.join(expected_extracted_dir2, file))

        # Check if the result contains the correct paths
        assert set(result) == {expected_extracted_dir1, expected_extracted_dir2}