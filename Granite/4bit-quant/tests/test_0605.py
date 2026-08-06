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
    # Test case 1: successful compilation
    filepath = 'test.cpp'
    task_func(filepath)
    assert logging.info.called
    assert 'Successfully compiled' in logging.info.call_args.args[0]

    # Test case 2: failed compilation due to subprocess error
    filepath = 'invalid_file.cpp'
    with pytest.raises(subprocess.CalledProcessError):
        task_func(filepath)
    assert logging.error.called
    assert 'Failed to compile' in logging.error.call_args.args[0]

    # Test case 3: failed compilation due to file not found error
    filepath = 'nonexistent_file.cpp'
    with pytest.raises(FileNotFoundError):
        task_func(filepath)
    assert logging.error.called
    assert 'Compiler not found or file does not exist' in logging.error.call_args.args[0]