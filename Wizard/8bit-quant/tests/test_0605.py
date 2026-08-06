python
import subprocess
import logging
import pytest

def task_func(filepath):
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Try to compile the C++ file
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)

    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)

def test_task_func():
    # Test case 1: Valid filepath
    task_func('test.cpp')
    assert True

    # Test case 2: Invalid filepath
    with pytest.raises(FileNotFoundError):
        task_func('invalid.cpp')

    # Test case 3: Compiler not found
    with pytest.raises(FileNotFoundError):
        task_func('test.c')