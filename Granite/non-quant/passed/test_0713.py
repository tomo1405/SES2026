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
    source_dir = "path/to/source/directory"
    dest_dir = "path/to/destination/directory"
    extension = "txt"
    
    result = task_func(source_dir, dest_dir, extension)
    
    assert result == 5  # Assuming there are 5 files with the .txt extension in the source directory