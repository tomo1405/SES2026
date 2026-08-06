import pytest
from src_0016 import task_func
import os
import csv
import tempfile
import subprocess

def create_temp_csv_file(commands):
    fd, temp_csv_path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w') as f:
        writer = csv.writer(f)
        for command in commands:
            writer.writerow([command])
    return temp_csv_path

def cleanup_temp_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except OSError:
            pass

def test_task_func_with_valid_input():
    # Create a temporary CSV file with some commands
    commands = ['echo "Hello, World!"', 'ls -l']
    commands_file_path = create_temp_csv_file(commands)
    
    # Create a temporary directory for output files
    with tempfile.TemporaryDirectory() as output_dir_path:
        # Call the function
        output_files = task_func(commands_file_path, output_dir_path)
        
        # Check if the output files exist and contain the expected content
        assert len(output_files) == len(commands)
        for output_file in output_files:
            assert os.path.exists(output_file)
            with open(output_file, 'r') as f:
                content = f.read()
                assert 'Hello, World!' in content
                assert 'total' in content  # This line is part of the 'ls -l' output

    # Cleanup temporary CSV file
    cleanup_temp_files([commands_file_path])

def test_task_func_with_non_existent_commands_file():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv', '/tmp')

def test_task_func_with_non_existent_output_dir():
    commands = ['echo "Hello, World!"']
    commands_file_path = create_temp_csv_file(commands)
    
    # Create a non-existent directory path
    output_dir_path = '/non_existent_dir'
    
    # Call the function
    output_files = task_func(commands_file_path, output_dir_path)
    
    # Check if the output directory was created and the output file exists
    assert os.path.exists(output_dir_path)
    assert len(output_files) == 1
    assert os.path.exists(output_files[0])

    # Cleanup temporary CSV file
    cleanup_temp_files([commands_file_path])

def test_task_func_with_error_command():
    commands = ['non_existent_command']
    commands_file_path = create_temp_csv_file(commands)
    
    # Create a temporary directory for output files
    with tempfile.TemporaryDirectory() as output_dir_path:
        # Call the function
        output_files = task_func(commands_file_path, output_dir_path)
        
        # Check if the output file exists and contains the error message
        assert len(output_files) == 1
        with open(output_files[0], 'r') as f:
            content = f.read()
            assert 'Error executing command, exited with code' in content

    # Cleanup temporary CSV file
    cleanup_temp_files([commands_file_path])