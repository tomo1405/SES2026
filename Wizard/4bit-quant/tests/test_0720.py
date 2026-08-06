python
import os
import glob
import re

def task_func(directory, word):
    count = 0
    # Pattern to match word boundaries and ignore case, handling punctuation
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    for filename in glob.glob(os.path.join(directory, '*.*')):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if pattern.search(text):
                count += 1
    return count

def test_task_func():
    # Test case 1: word is present in a file
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test".')
    assert task_func(directory, 'test') == 1
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 2: word is not present in a file
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It does not contain the word "test".')
    assert task_func(directory, 'test') == 0
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 3: word is present in multiple files
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test".')
    with open(os.path.join(directory, 'file2.txt'), 'w', encoding='utf-8') as f:
        f.write('This is another test file. It also contains the word "test".')
    assert task_func(directory, 'test') == 2
    os.remove(os.path.join(directory, 'file1.txt'))
    os.remove(os.path.join(directory, 'file2.txt'))
    os.rmdir(directory)

    # Test case 4: word is present in a file with different capitalization
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "Test".')
    assert task_func(directory, 'test') == 1
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 5: word is present in a file with punctuation
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test,".')
    assert task_func(directory, 'test') == 1
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 6: word is present in a file with multiple occurrences
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test". It also contains the word "test".')
    assert task_func(directory, 'test') == 2
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 7: word is present in a file with different capitalization and punctuation
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "Test,".')
    assert task_func(directory, 'test') == 1
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 8: word is present in a file with different capitalization and punctuation and multiple occurrences
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "Test,". It also contains the word "test,".')
    assert task_func(directory, 'test') == 2
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 9: directory does not exist
    directory = 'test_dir'
    assert task_func(directory, 'test') == 0

    # Test case 10: directory is empty
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    assert task_func(directory, 'test') == 0
    os.rmdir(directory)

    # Test case 11: word is not a string
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test".')
    try:
        task_func(directory, 123)
    except TypeError:
        assert True
    else:
        assert False
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 12: word is an empty string
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test".')
    try:
        task_func(directory, '')
    except ValueError:
        assert True
    else:
        assert False
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)

    # Test case 13: word is a string with non-alphanumeric characters
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w', encoding='utf-8') as f:
        f.write('This is a test file. It contains the word "test".')
    try:
        task_func(directory, 'test#')
    except ValueError:
        assert True
    else:
        assert False
    os.remove(os.path.join(directory, 'file1.txt'))
    os.rmdir(directory)