import codecs
import os
import tempfile
import zipfile

from src_0763 import task_func


def test_task_func():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change the current working directory to the temporary directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)

        # Call the function
        zipped_file = task_func()

        # Check if the zip file exists
        assert os.path.exists(zipped_file)

        # Unzip the file to check contents
        with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Check if all files are created and have the correct content
        for file_name in ['file1.txt', 'file2.txt', 'file3.txt']:
            file_path = os.path.join(temp_dir, directory_name, file_name)
            assert os.path.exists(file_path)
            with open(file_path, 'rb') as f:
                content = f.read()
                assert content == codecs.encode('Sopetón', 'latin-1')

        # Restore the original working directory
        os.chdir(original_cwd)