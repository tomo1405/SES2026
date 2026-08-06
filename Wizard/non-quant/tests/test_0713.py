python
import os
import shutil
import glob
import pytest

def task_func(source_dir, dest_dir, extension):
    files = glob.glob(os.path.join(source_dir, f'*.{extension}'))
    
    for file in files:
        shutil.move(file, dest_dir)
        
    result = len(files)

    return result

def test_task_func():
    source_dir = 'tests/test_files'
    dest_dir = 'tests/test_files_moved'
    extension = 'txt'
    
    # Test case 1: Move all .txt files from source_dir to dest_dir
    result = task_func(source_dir, dest_dir, extension)
    assert result == 2
    
    # Test case 2: Move all .txt files from source_dir to dest_dir again
    result = task_func(source_dir, dest_dir, extension)
    assert result == 2
    
    # Test case 3: Move all .txt files from source_dir to dest_dir with a different extension
    extension = 'csv'
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 4: Move all .txt files from source_dir to dest_dir with a different extension again
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 5: Move all .txt files from source_dir to dest_dir with a different extension and a different source directory
    source_dir = 'tests/test_files_2'
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 6: Move all .txt files from source_dir to dest_dir with a different extension and a different source directory again
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 7: Move all .txt files from source_dir to dest_dir with a different extension and a different destination directory
    dest_dir = 'tests/test_files_moved_2'
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 8: Move all .txt files from source_dir to dest_dir with a different extension and a different destination directory again
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 9: Move all .txt files from source_dir to dest_dir with a different extension and a different source and destination directory
    source_dir = 'tests/test_files_3'
    dest_dir = 'tests/test_files_moved_3'
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1
    
    # Test case 10: Move all .txt files from source_dir to dest_dir with a different extension and a different source and destination directory again
    result = task_func(source_dir, dest_dir, extension)
    assert result == 1