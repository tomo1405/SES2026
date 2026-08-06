python
import os
import glob
import zipfile
import pytest

def task_func(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")
    files = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.isfile(f)]
    if not files:
        return None
    zip_file_path = os.path.join(directory, 'files.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    return zip_file_path

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')
    
    # Test case 2: Directory is empty
    with pytest.raises(ValueError):
        task_func('empty_directory')
    
    # Test case 3: Directory contains only one file
    file_path = os.path.join('directory_with_one_file', 'file.txt')
    with open(file_path, 'w') as f:
        f.write('Hello, world!')
    assert task_func('directory_with_one_file') == os.path.join('directory_with_one_file', 'files.zip')
    
    # Test case 4: Directory contains multiple files
    file_path1 = os.path.join('directory_with_multiple_files', 'file1.txt')
    file_path2 = os.path.join('directory_with_multiple_files', 'file2.txt')
    with open(file_path1, 'w') as f:
        f.write('Hello, world!')
    with open(file_path2, 'w') as f:
        f.write('Goodbye, world!')
    assert task_func('directory_with_multiple_files') == os.path.join('directory_with_multiple_files', 'files.zip')