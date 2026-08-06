import pytest
from src_0907 import task_func

def test_task_func():
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    archive_name = 'archive.zip'
    
    # Create directories
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    # Create test files
    test_file_1 = 'test_file_1.txt'
    test_file_2 = 'test_file_2.txt'
    test_file_3 = 'test_file_3.txt'
    test_file_4 = 'test_file_4.txt'
    test_file_5 = 'test_file_5.txt'
    test_file_6 = 'test_file_6.txt'
    test_file_7 = 'test_file_7.txt'
    test_file_8 = 'test_file_8.txt'
    test_file_9 = 'test_file_9.txt'
    test_file_10 = 'test_file_10.txt'
    
    # Create test files in source directory
    with open(os.path.join(source_dir, test_file_1), 'w') as f:
        f.write('test_file_1')
    with open(os.path.join(source_dir, test_file_2), 'w') as f:
        f.write('test_file_2')
    with open(os.path.join(source_dir, test_file_3), 'w') as f:
        f.write('test_file_3')
    with open(os.path.join(source_dir, test_file_4), 'w') as f:
        f.write('test_file_4')
    with open(os.path.join(source_dir, test_file_5), 'w') as f:
        f.write('test_file_5')
    with open(os.path.join(source_dir, test_file_6), 'w') as f:
        f.write('test_file_6')
    with open(os.path.join(source_dir, test_file_7), 'w') as f:
        f.write('test_file_7')
    with open(os.path.join(source_dir, test_file_8), 'w') as f:
        f.write('test_file_8')
    with open(os.path.join(source_dir, test_file_9), 'w') as f:
        f.write('test_file_9')
    with open(os.path.join(source_dir, test_file_10), 'w') as f:
        f.write('test_file_10')
    
    # Run task function
    archive_path = task_func(source_dir, target_dir, archive_name)
    
    # Check that the archive file was created
    assert os.path.isfile(archive_path)
    
    # Check that the files were moved to the target directory
    assert not os.path.isfile(os.path.join(source_dir, test_file_1))
    assert not os.path.isfile(os.path.join(source_dir, test_file_2))
    assert not os.path.isfile(os.path.join(source_dir, test_file_3))
    assert not os.path.isfile(os.path.join(source_dir, test_file_4))
    assert not os.path.isfile(os.path.join(source_dir, test_file_5))
    assert not os.path.isfile(os.path.join(source_dir, test_file_6))
    assert not os.path.isfile(os.path.join(source_dir, test_file_7))
    assert not os.path.isfile(os.path.join(source_dir, test_file_8))
    assert not os.path.isfile(os.path.join(source_dir, test_file_9))
    assert not os.path.isfile(os.path.join(source_dir, test_file_10))
    
    # Check that the files were added to the archive
    with zipfile.ZipFile(archive_path, 'r') as archive:
        assert archive.namelist() == [test_file_1, test_file_2, test_file_3, test_file_4, test_file_5, test_file_6, test_file_7, test_file_8, test_file_9, test_file_10]