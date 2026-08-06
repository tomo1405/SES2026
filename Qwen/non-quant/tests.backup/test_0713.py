import pytest
from src_0713 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary source directory and destination directory
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some test files in the source directory
        test_files = [
            'file1.txt',
            'file2.txt',
            'file3.docx',
            'file4.txt'
        ]
        for file in test_files:
            with open(os.path.join(source_dir, file), 'w') as f:
                f.write('Test content')

        # Define the extension to move
        extension = 'txt'

        # Call the function
        result = task_func(source_dir, dest_dir, extension)

        # Check that the correct number of files were moved
        assert result == 3

        # Check that the files with the specified extension are in the destination directory
        dest_files = os.listdir(dest_dir)
        expected_files = ['file1.txt', 'file2.txt', 'file4.txt']
        assert sorted(dest_files) == sorted(expected_files)

        # Check that the files with the specified extension are no longer in the source directory
        remaining_files = os.listdir(source_dir)
        assert remaining_files == ['file3.docx']

# Run the tests
if __name__ == "__main__":
    pytest.main()