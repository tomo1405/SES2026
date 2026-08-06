python
import os
import logging
import pytest

def task_func(directory):

    # Configure logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Get all files in the directory
    files = os.listdir(directory)

    # Remove jQuery files
    removed_files = 0
    removed_file_names = []
    for file in files:
        if 'jquery' in file and file.endswith('.js'):
            try:
                os.remove(os.path.join(directory, file))
                removed_files += 1
                removed_file_names.append(file)
                logging.info(f"Removed jQuery file: {file}")
            except Exception as e:
                logging.error(f"Error while removing file {file}: {e}")

    return removed_files, removed_file_names

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')

    # Test case 2: Directory exists but has no jQuery files
    directory = 'tests/test_data/no_jquery_files'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 0
    assert removed_file_names == []

    # Test case 3: Directory exists and has jQuery files
    directory = 'tests/test_data/jquery_files'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 2
    assert removed_file_names == ['jquery-1.11.0.min.js', 'jquery-2.2.0.min.js']

    # Test case 4: Directory exists and has jQuery files but some cannot be removed
    directory = 'tests/test_data/jquery_files_with_errors'
    removed_files, removed_file_names = task_func(directory)
    assert removed_files == 1
    assert removed_file_names == ['jquery-1.11.0.min.js']