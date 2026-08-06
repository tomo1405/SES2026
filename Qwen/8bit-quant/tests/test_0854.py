import pytest
from src_0854 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directory():
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'Invalid'))
    os.makedirs(os.path.join(temp_dir, 'txt'))
    os.makedirs(os.path.join(temp_dir, 'jpg'))
    
    # Create files with different names and extensions
    with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file2.jpg'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file3!@#.txt'), 'w') as f:
        f.write('content')
    with open(os.path.join(temp_dir, 'file4.docx'), 'w') as f:
        f.write('content')
    
    yield temp_dir
    
    # Clean up
    shutil.rmtree(temp_dir)

def test_task_func(setup_directory):
    directory_path = setup_directory
    result = task_func(directory_path)
    
    # Check if files are moved correctly
    assert not os.path.exists(os.path.join(directory_path, 'file1.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file2.jpg'))
    assert not os.path.exists(os.path.join(directory_path, 'file3!@#.txt'))
    assert not os.path.exists(os.path.join(directory_path, 'file4.docx'))
    
    assert os.path.exists(os.path.join(directory_path, 'txt', 'file1.txt'))
    assert os.path.exists(os.path.join(directory_path, 'jpg', 'file2.jpg'))
    assert os.path.exists(os.path.join(directory_path, 'Invalid', 'file3!@#.txt'))
    assert os.path.exists(os.path.join(directory_path, 'docx', 'file4.docx'))
    
    # Check the summary
    expected_summary = {
        'txt': 1,
        'jpg': 1,
        'Invalid': 1,
        'docx': 1
    }
    assert result == expected_summary