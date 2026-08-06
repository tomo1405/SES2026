import csv
import glob
import os
import subprocess
import tempfile

from src_0019 import task_func


def test_task_func_nonexistent_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'nonexistent.csv')
        result = task_func(file_path)
        assert result == [], "Should return an empty list for a non-existent file"

def test_task_func_non_csv_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'file.txt')
        with open(file_path, 'w') as f:
            f.write("This is a text file")
        result = task_func(file_path)
        assert result == [], "Should return an empty list for a non-CSV file"

def test_task_func_valid_csv_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'data.csv')
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Age'])
            writer.writerow(['Alice', '30'])
            writer.writerow(['Bob', '25'])

        result = task_func(file_path)
        assert len(result) == 5, "Should return 5 split files"
        for split_file in result:
            assert os.path.exists(split_file), "Split file should exist"
            with open(split_file, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
                assert len(rows) <= 2, "Each split file should have at most 2 rows"
        glob.glob('split_*')

def test_task_func_exception_handling():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'data.csv')
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Age'])
            writer.writerow(['Alice', '30'])
            writer.writerow(['Bob', '25'])

        # Mocking subprocess call to raise an exception
        def mock_subprocess_call(*args, **kwargs):
            raise Exception("Mocked exception")

        original_subprocess_call = subprocess.call
        subprocess.call = mock_subprocess_call

        result = task_func(file_path)
        assert result == [], "Should return an empty list on exception"

        subprocess.call = original_subprocess_call