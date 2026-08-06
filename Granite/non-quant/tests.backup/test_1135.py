import os
import glob
import hashlib
import pytest
from src_1135 import task_func

def test_task_func():
    source_dir = "source_directory"
    target_dir = "target_directory"
    prefix = "#Hash: "
    new_files = task_func(source_dir, target_dir, prefix)
    
    assert os.path.exists(source_dir), "Source directory does not exist"
    assert os.path.exists(target_dir), "Target directory does not exist"
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        with open(file_path, 'r') as infile:
            content = infile.read()
        
        hash_object = hashlib.md5(content.encode())
        new_file_path = os.path.join(target_dir, os.path.basename(file_path))
        
        with open(new_file_path, 'r') as outfile:
            output_content = outfile.read()
        
        assert output_content.startswith(prefix), "Output file does not start with the specified prefix"
        assert output_content.split('\n')[0] == f"{prefix}{hash_object.hexdigest()}", "Output file does not contain the correct hash"
        assert output_content.split('\n')[1] == content, "Output file does not contain the correct content"
    
    assert len(new_files) > 0, "No new files were created"