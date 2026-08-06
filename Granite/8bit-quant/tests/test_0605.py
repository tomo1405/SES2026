import subprocess
import logging
from src_0605 import task_func

def test_task_func_with_valid_file():
    filepath = 'test.cpp'
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)
    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)

def test_task_func_with_invalid_file():
    filepath = 'invalid_file.cpp'
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)
    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)

def test_task_func_with_compiler_not_found():
    filepath = 'test.cpp'
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)
    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)