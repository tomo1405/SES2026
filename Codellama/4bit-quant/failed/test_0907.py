import pytest
from src_0907 import task_func

def test_task_func():
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    archive_name = 'archive.zip'
    
    # Create directories
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    # Create files in source directory
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    file3 = 'file3.txt'
    file4 = 'file4.txt'
    file5 = 'file5.txt'
    file6 = 'file6.txt'
    file7 = 'file7.txt'
    file8 = 'file8.txt'
    file9 = 'file9.txt'
    file10 = 'file10.txt'
    
    with open(os.path.join(source_dir, file1), 'w') as f:
        f.write('file1')
    with open(os.path.join(source_dir, file2), 'w') as f:
        f.write('file2')
    with open(os.path.join(source_dir, file3), 'w') as f:
        f.write('file3')
    with open(os.path.join(source_dir, file4), 'w') as f:
        f.write('file4')
    with open(os.path.join(source_dir, file5), 'w') as f:
        f.write('file5')
    with open(os.path.join(source_dir, file6), 'w') as f:
        f.write('file6')
    with open(os.path.join(source_dir, file7), 'w') as f:
        f.write('file7')
    with open(os.path.join(source_dir, file8), 'w') as f:
        f.write('file8')
    with open(os.path.join(source_dir, file9), 'w') as f:
        f.write('file9')
    with open(os.path.join(source_dir, file10), 'w') as f:
        f.write('file10')
    
    # Run task function
    archive_path = task_func(source_dir, target_dir, archive_name)
    
    # Check that the archive was created
    assert os.path.exists(archive_path)
    
    # Check that the files were moved to the target directory
    assert os.path.exists(os.path.join(target_dir, file1))
    assert os.path.exists(os.path.join(target_dir, file2))
    assert os.path.exists(os.path.join(target_dir, file3))
    assert os.path.exists(os.path.join(target_dir, file4))
    assert os.path.exists(os.path.join(target_dir, file5))
    assert os.path.exists(os.path.join(target_dir, file6))
    assert os.path.exists(os.path.join(target_dir, file7))
    assert os.path.exists(os.path.join(target_dir, file8))
    assert os.path.exists(os.path.join(target_dir, file9))
    assert os.path.exists(os.path.join(target_dir, file10))
    
    # Check that the files were not moved to the source directory
    assert not os.path.exists(os.path.join(source_dir, file1))
    assert not os.path.exists(os.path.join(source_dir, file2))
    assert not os.path.exists(os.path.join(source_dir, file3))
    assert not os.path.exists(os.path.join(source_dir, file4))
    assert not os.path.exists(os.path.join(source_dir, file5))
    assert not os.path.exists(os.path.join(source_dir, file6))
    assert not os.path.exists(os.path.join(source_dir, file7))
    assert not os.path.exists(os.path.join(source_dir, file8))
    assert not os.path.exists(os.path.join(source_dir, file9))
    assert not os.path.exists(os.path.join(source_dir, file10))
    
    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)
    os.remove(archive_path)