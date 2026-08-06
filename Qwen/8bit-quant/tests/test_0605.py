import subprocess
from unittest.mock import patch

from src_0605 import task_func


def test_task_func_success(tmp_path):
    # Create a temporary C++ file
    c_file = tmp_path / "test.cpp"
    c_file.write_text("int main() { return 0; }")

    with patch('subprocess.check_call') as mock_check_call, \
         patch('logging.info') as mock_info, \
         patch('logging.error') as mock_error:
        
        task_func(str(c_file))

        mock_check_call.assert_called_once_with(['g++', str(c_file), '-o', 'test'])
        mock_info.assert_called_once_with('Successfully compiled %s', str(c_file))
        mock_error.assert_not_called()

def test_task_func_compile_failure(tmp_path):
    # Create a temporary C++ file with a syntax error
    c_file = tmp_path / "test.cpp"
    c_file.write_text("int main() { return 0")

    with patch('subprocess.check_call') as mock_check_call, \
         patch('logging.info') as mock_info, \
         patch('logging.error') as mock_error:
        
        mock_check_call.side_effect = subprocess.CalledProcessError(1, ['g++', str(c_file), '-o', 'test'])

        task_func(str(c_file))

        mock_check_call.assert_called_once_with(['g++', str(c_file), '-o', 'test'])
        mock_info.assert_not_called()
        mock_error.assert_called_once_with('Failed to compile %s: %s', str(c_file), mock_check_call.side_effect)

def test_task_func_file_not_found(tmp_path):
    # Use a non-existent file path
    c_file = tmp_path / "non_existent.cpp"

    with patch('subprocess.check_call') as mock_check_call, \
         patch('logging.info') as mock_info, \
         patch('logging.error') as mock_error:
        
        mock_check_call.side_effect = FileNotFoundError("No such file or directory")

        task_func(str(c_file))

        mock_check_call.assert_called_once_with(['g++', str(c_file), '-o', 'non_existent'])
        mock_info.assert_not_called()
        mock_error.assert_called_once_with('Compiler not found or file does not exist: No such file or directory')