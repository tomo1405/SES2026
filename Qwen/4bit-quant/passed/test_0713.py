import pytest
from src_0713 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary source directory
    with tempfile.TemporaryDirectory() as source_dir:
        # Create a temporary destination directory
        with tempfile.TemporaryDirectory() as dest_dir:
            # Create some test files in the source directory
            test_files = [
                os.path.join(source_dir, 'file1.txt'),
                os.path.join(source_dir, 'file2.txt'),
                os.path.join(source_dir, 'file3.doc')
            ]
            for file in test_files:
                open(file, 'a').close()

            # Call the function with '.txt' extension
            result = task_func(source_dir, dest_dir, 'txt')

            # Check if the files were moved correctly
            assert not os.path.exists(test_files[0])
            assert not os.path.exists(test_files[1])
            assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
            assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))

            # Check if the non-matching file is still in the source directory
            assert os.path.exists(test_files[2])

            # Check if the result is correct
            assert result == 2

# Run the tests
if __name__ == '__main__':
    pytest.main()