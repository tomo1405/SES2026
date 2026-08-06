python
import pytest
from src_0999 import task_func

def test_task_func():
    # Test case 1: Valid URL
    url = "https://www.google.com"
    assert task_func(url) == True

    # Test case 2: Invalid URL
    url = "https://www.google.com/invalid"
    assert task_func(url) == False

    # Test case 3: Valid URL with invalid MD5 checksum
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'invalid_checksum'\n")
    assert task_func(url) == False

    # Test case 4: Valid URL with valid MD5 checksum
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'd41d8cd98f00b204e9800998ecf8427e'\n")
    assert task_func(url) == True

    # Test case 5: Valid URL with valid MD5 checksum and invalid tar file
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'd41d8cd98f00b204e9800998ecf8427e'\n")
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import tarfile\nwith open('downloaded_files.tar.gz', 'w') as f:\n    f.write('invalid_tar_file')\n")
    assert task_func(url) == False

    # Test case 6: Valid URL with valid MD5 checksum and valid tar file
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'd41d8cd98f00b204e9800998ecf8427e'\n")
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import tarfile\nwith open('downloaded_files.tar.gz', 'w') as f:\n    f.write('invalid_tar_file')\n")
    with open('downloaded_files.tar.gz', 'w') as f:
        f.write('valid_tar_file')
    assert task_func(url) == True

    # Test case 7: Valid URL with valid MD5 checksum and valid tar file but invalid extraction
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'd41d8cd98f00b204e9800998ecf8427e'\n")
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import tarfile\nwith open('downloaded_files.tar.gz', 'w') as f:\n    f.write('invalid_tar_file')\n")
    with open('downloaded_files.tar.gz', 'w') as f:
        f.write('valid_tar_file')
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import os\nimport shutil\nshutil.rmtree('extracted_files')\n")
    assert task_func(url) == False

    # Test case 8: Valid URL with valid MD5 checksum and valid tar file and valid extraction
    url = "https://www.google.com"
    with open(task_func.__code__.co_filename, "w") as f:
        f.write("import hashlib\nEXPECTED_MD5_CHECKSUM = 'd41d8cd98f00b204e9800998ecf8427e'\n")
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import tarfile\nwith open('downloaded_files.tar.gz', 'w') as f:\n    f.write('invalid_tar_file')\n")
    with open('downloaded_files.tar.gz', 'w') as f:
        f.write('valid_tar_file')
    with open(task_func.__code__.co_filename, "a") as f:
        f.write("import os\nimport shutil\nshutil.rmtree('extracted_files')\n")
    with open('extracted_files/file.txt', 'w') as f:
        f.write('valid_extraction')
    assert task_func(url) == True