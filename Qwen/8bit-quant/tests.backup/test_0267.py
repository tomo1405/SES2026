import pytest
from src_0267 import task_func
import os
import tempfile
import csv

def test_task_func():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with known sizes
        file1 = os.path.join(temp_dir, 'file1.txt')
        file2 = os.path.join(temp_dir, 'file2.txt')
        with open(file1, 'w') as f:
            f.write('Hello, world!')  # 13 bytes
        with open(file2, 'w') as f:
            f.write('Goodbye, world!')  # 14 bytes

        # Call the function
        output_file = task_func(temp_dir)

        # Check that the output file was created
        assert os.path.exists(output_file)

        # Read the contents of the output file
        with open(output_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        # Check the header row
        assert rows[0] == ['File Name', 'Size']

        # Check the data rows
        assert sorted(rows[1:]) == [['file1.txt', '13'], ['file2.txt', '14']]