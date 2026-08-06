import pytest
from src_0760 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary source directory
    with tempfile.TemporaryDirectory() as source_dir:
        # Create a temporary destination directory
        with tempfile.TemporaryDirectory() as dest_dir:
            # Create some files in the source directory
            file1 = os.path.join(source_dir, 'file1.txt')
            file2 = os.path.join(source_dir, 'file2.log')
            file3 = os.path.join(source_dir, 'subdir', 'file3.txt')
            os.makedirs(os.path.dirname(file3))
            open(file1, 'a').close()
            open(file2, 'a').close()
            open(file3, 'a').close()

            # Define the file pattern to match
            file_pattern = '*.txt'

            # Call the function
            moved_files = task_func(source_dir, dest_dir, file_pattern)

            # Check that the correct files were moved
            assert moved_files == ['file1.txt', 'file3.txt']
            assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
            assert os.path.exists(os.path.join(dest_dir, 'file3.txt'))
            assert not os.path.exists(file1)
            assert not os.path.exists(file3)

            # Check that the file2.log was not moved
            assert os.path.exists(file2)

# Run the test
if __name__ == "__main__":
    pytest.main()