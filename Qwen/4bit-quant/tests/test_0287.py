import pytest
from src_0287 import task_func
import os
import csv
import tempfile

def create_temp_files(directory, files):
    for file_name, content in files.items():
        with open(os.path.join(directory, file_name), 'w') as file:
            file.write(content)

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def test_task_func():
    # Create a temporary directory and some text files
    with tempfile.TemporaryDirectory() as temp_dir:
        files = {
            'file1.txt': 'hello world hello',
            'file2.txt': 'world world',
            'file3.csv': 'not a text file'
        }
        create_temp_files(temp_dir, files)

        output_file = os.path.join(temp_dir, 'output.csv')
        total_words = task_func(output_file, temp_dir)

        # Check if the output file is created and contains the correct data
        assert os.path.exists(output_file)
        csv_data = read_csv(output_file)
        expected_header = ['Word', 'Count']
        expected_rows = [
            ['hello', '2'],
            ['world', '3']
        ]
        assert csv_data[0] == expected_header
        assert sorted(csv_data[1:]) == sorted(expected_rows)

        # Check if the total words count is correct
        assert total_words == 5

def test_task_func_no_text_files():
    # Create a temporary directory with no text files
    with tempfile.TemporaryDirectory() as temp_dir:
        files = {
            'file1.csv': 'not a text file',
            'file2.jpg': 'image file'
        }
        create_temp_files(temp_dir, files)

        output_file = os.path.join(temp_dir, 'output.csv')
        total_words = task_func(output_file, temp_dir)

        # Check if the output file is created and is empty
        assert os.path.exists(output_file)
        csv_data = read_csv(output_file)
        expected_header = ['Word', 'Count']
        assert csv_data == [expected_header]

        # Check if the total words count is zero
        assert total_words == 0

def test_task_func_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = os.path.join(temp_dir, 'output.csv')
        total_words = task_func(output_file, temp_dir)

        # Check if the output file is created and is empty
        assert os.path.exists(output_file)
        csv_data = read_csv(output_file)
        expected_header = ['Word', 'Count']
        assert csv_data == [expected_header]

        # Check if the total words count is zero
        assert total_words == 0

def test_task_func_exception_handling():
    # Create a temporary directory with a non-readable file
    with tempfile.TemporaryDirectory() as temp_dir:
        files = {
            'file1.txt': 'hello world'
        }
        create_temp_files(temp_dir, files)

        # Make the file non-readable
        file_path = os.path.join(temp_dir, 'file1.txt')
        os.chmod(file_path, 0o000)

        output_file = os.path.join(temp_dir, 'output.csv')
        total_words = task_func(output_file, temp_dir)

        # Check if the output file is created and is empty
        assert os.path.exists(output_file)
        csv_data = read_csv(output_file)
        expected_header = ['Word', 'Count']
        assert csv_data == [expected_header]

        # Check if the total words count is zero
        assert total_words == 0