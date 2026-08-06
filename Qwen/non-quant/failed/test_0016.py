import pytest
from src_0016 import task_func
import os
import tempfile
import csv

def test_task_func_nonexistent_commands_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "nonexistent_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with pytest.raises(FileNotFoundError):
            task_func(commands_file_path, output_dir_path)

def test_task_func_empty_commands_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "empty_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([])  # Empty row
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 1
        assert os.path.exists(output_files[0])
        with open(output_files[0], 'r') as f:
            content = f.read()
            assert "Error executing command, exited with code" in content

def test_task_func_single_command_success():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "single_command.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["echo Hello, World!"])
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 1
        assert os.path.exists(output_files[0])
        with open(output_files[0], 'r') as f:
            content = f.read()
            assert "Hello, World!" in content

def test_task_func_multiple_commands():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "multiple_commands.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["echo First command"])
            writer.writerow(["echo Second command"])
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 2
        for i, output_file in enumerate(output_files):
            assert os.path.exists(output_file)
            with open(output_file, 'r') as f:
                content = f.read()
                assert f"command_{i+1}_output.txt" in output_file
                if i == 0:
                    assert "First command" in content
                elif i == 1:
                    assert "Second command" in content

def test_task_func_command_failure():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "command_failure.csv")
        output_dir_path = os.path.join(temp_dir, "output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["invalid_command"])
        output_files = task_func(commands_file_path, output_dir_path)
        assert len(output_files) == 1
        assert os.path.exists(output_files[0])
        with open(output_files[0], 'r') as f:
            content = f.read()
            assert "Error executing command, exited with code" in content

def test_task_func_output_directory_creation():
    with tempfile.TemporaryDirectory() as temp_dir:
        commands_file_path = os.path.join(temp_dir, "commands.csv")
        output_dir_path = os.path.join(temp_dir, "nonexistent_output")
        with open(commands_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["echo Test"])
        task_func(commands_file_path, output_dir_path)
        assert os.path.exists(output_dir_path)