import pytest
from src_0713 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    source_dir = 'test_source'
    dest_dir = 'test_dest'
    extension = 'txt'
    
    # Create a sample file in the source directory
    os.makedirs(source_dir)
    with open(os.path.join(source_dir, 'testfile.txt'), 'w') as f:
        f.write('test')
    
    result = task_func(source_dir, dest_dir, extension)
    
    assert result == 1
    
    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)

# Add more test cases as needed