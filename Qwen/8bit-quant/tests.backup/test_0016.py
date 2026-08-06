import pytest
from src_0016 import task_func
import os
import tempfile
import csv

def test_task_func_with_nonexistent_commands_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "nonexistent_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with pytest.raises(FileNotFoundError):
            task_func(commands_file_path, output_dir_path)

def test_task_func_with_empty_commands_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "empty_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([])  # Empty row
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 0

def test_task_func_with_valid_commands():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "valid_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["echo Hello, World!"])
            writer.writerow(["echo Goodbye, World!"])
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 2
        for output_file in output_files:
            assert os.path.exists(output_file)
            with open(output_file, 'r') as f:
                content = f.read()
                assert "Hello, World!" in content
                assert "Goodbye, World!" in content

def test_task_func_with_command_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "error_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["invalid_command"])  # This should fail
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 1
        with open(output_files[0], 'r') as f:
            content = f.read()
            assert "Error executing command, exited with code" in content

def test_task_func_with_existing_output_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "valid_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        os.makedirs(output_dir_path)  # Ensure the directory already exists
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["echo Hello, World!"])
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 1
        assert os.path.exists(output_files[0])