import pytest
from src_0015 import task_func
import os
import tempfile
import configparser

def test_task_func_with_valid_config():
    # Create a temporary directory and a config file
    with tempfile.TemporaryDirectory() as temp_dir:
        config_content = """
        [Project]
        directory = {temp_dir}
        """.format(temp_dir=temp_dir)
        
        config_file_path = os.path.join(temp_dir, 'config.ini')
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
        
        # Call the function
        result = task_func(config_file_path, temp_dir)
        
        # Check if the result is True
        assert result is True
        
        # Check if the archive file exists
        archive_file = os.path.join(temp_dir, os.path.basename(temp_dir) + '.zip')
        assert os.path.isfile(archive_file)

def test_task_func_with_invalid_directory():
    # Create a temporary directory and a config file with an invalid directory
    with tempfile.TemporaryDirectory() as temp_dir:
        config_content = """
        [Project]
        directory = /non/existing/directory
        """
        
        config_file_path = os.path.join(temp_dir, 'config.ini')
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
        
        # Expect a FileNotFoundError
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(config_file_path, temp_dir)
        
        # Check the error message
        assert str(excinfo.value) == "Directory /non/existing/directory does not exist."

def test_task_func_with_missing_config_section():
    # Create a temporary directory and a config file without the Project section
    with tempfile.TemporaryDirectory() as temp_dir:
        config_content = """
        [OtherSection]
        key = value
        """
        
        config_file_path = os.path.join(temp_dir, 'config.ini')
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
        
        # Expect a NoSectionError
        with pytest.raises(configparser.NoSectionError) as excinfo:
            task_func(config_file_path, temp_dir)
        
        # Check the error message
        assert str(excinfo.value) == "No section: 'Project'"

def test_task_func_with_missing_config_key():
    # Create a temporary directory and a config file without the directory key
    with tempfile.TemporaryDirectory() as temp_dir:
        config_content = """
        [Project]
        other_key = value
        """
        
        config_file_path = os.path.join(temp_dir, 'config.ini')
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
        
        # Expect a NoOptionError
        with pytest.raises(configparser.NoOptionError) as excinfo:
            task_func(config_file_path, temp_dir)
        
        # Check the error message
        assert str(excinfo.value) == "No option 'directory' in section: 'Project'"