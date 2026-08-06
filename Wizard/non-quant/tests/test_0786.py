python
import subprocess
import os
import glob

# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Create archive directory if it does not exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Get the list of files matching the pattern
    file_list = glob.glob(pattern)
    
    if not file_list:
        return "No files found matching the pattern."

    # Create a unique archive file name
    archive_file_base = os.path.join(ARCHIVE_DIR, 'archive')
    archive_file = archive_file_base + '.tar.gz'
    counter = 1
    while os.path.exists(archive_file):
        archive_file = archive_file_base + f"_{counter}.tar.gz"
        counter += 1
    
    # Create an archive file
    subprocess.run(['tar', '-czf', archive_file] + file_list)
    
    # Delete the original files
    for file in file_list:
        os.remove(file)
    
    return archive_file

# Test the function
def test_task_func():
    # Test case 1: Archive a single file
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    assert task_func(file_path) == '/tmp/archive/archive.tar.gz'
    os.remove(file_path)

    # Test case 2: Archive multiple files
    file_path1 = '/tmp/test1.txt'
    file_path2 = '/tmp/test2.txt'
    with open(file_path1, 'w') as f:
        f.write('test1')
    with open(file_path2, 'w') as f:
        f.write('test2')
    assert task_func(f'{file_path1} {file_path2}') == '/tmp/archive/archive.tar.gz'
    os.remove(file_path1)
    os.remove(file_path2)

    # Test case 3: Archive no files
    assert task_func('/tmp/nonexistent_file.txt') == 'No files found matching the pattern.'

    # Test case 4: Archive a file with spaces in its name
    file_path = '/tmp/test file.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    assert task_func(file_path) == '/tmp/archive/archive.tar.gz'
    os.remove(file_path)

    # Test case 5: Archive a file with special characters in its name
    file_path = '/tmp/test#file.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    assert task_func(file_path) == '/tmp/archive/archive.tar.gz'
    os.remove(file_path)

    # Test case 6: Archive a file with a name that already exists in the archive directory
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    os.makedirs('/tmp/archive/archive.tar.gz')
    assert task_func(file_path) == '/tmp/archive/archive_1.tar.gz'
    os.remove(file_path)
    os.rmdir('/tmp/archive/archive.tar.gz')

    # Test case 7: Archive a file with a name that already exists in the archive directory with a number
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    os.makedirs('/tmp/archive/archive_1.tar.gz')
    assert task_func(file_path) == '/tmp/archive/archive_2.tar.gz'
    os.remove(file_path)
    os.rmdir('/tmp/archive/archive_1.tar.gz')

    # Test case 8: Archive a file with a name that already exists in the archive directory with a number and a suffix
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    os.makedirs('/tmp/archive/archive_1.tar.gz.bak')
    assert task_func(file_path) == '/tmp/archive/archive_2.tar.gz'
    os.remove(file_path)
    os.rmdir('/tmp/archive/archive_1.tar.gz.bak')

    # Test case 9: Archive a file with a name that already exists in the archive directory with a number and a suffix and a prefix
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    os.makedirs('/tmp/archive/archive_1.tar.gz.bak.old')
    assert task_func(file_path) == '/tmp/archive/archive_2.tar.gz'
    os.remove(file_path)
    os.rmdir('/tmp/archive/archive_1.tar.gz.bak.old')

    # Test case 10: Archive a file with a name that already exists in the archive directory with a number and a suffix and a prefix and a suffix
    file_path = '/tmp/test.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    os.makedirs('/tmp/archive/archive_1.tar.gz.bak.old.bak')
    assert task_func(file_path) == '/tmp/archive/archive_2.tar.gz'
    os.remove(file_path)
    os.rmdir('/tmp/archive/archive_1.tar.gz.bak.old.bak')