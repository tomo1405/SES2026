python
import os
from datetime import datetime
import pytest

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):

    if not isinstance(metrics, dict):
        raise ValueError("Metrics must be a dictionary")
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string")
    
    try:
        with open(os.path.join(log_dir, filename), 'a') as f:
            f.write(f'{datetime.now()}\n')
            for key, value in metrics.items():
                f.write(f'{key}: {value}\n')
            f.write('\n')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def test_task_func():
    # Test case 1: Valid input
    metrics = {'accuracy': 0.9, 'loss': 0.05}
    filename = 'metrics.txt'
    assert task_func(metrics, filename) == True
    
    # Test case 2: Invalid input (metrics is not a dictionary)
    metrics = 'not a dictionary'
    filename = 'metrics.txt'
    with pytest.raises(ValueError):
        task_func(metrics, filename)
    
    # Test case 3: Invalid input (filename is not a string)
    metrics = {'accuracy': 0.9, 'loss': 0.05}
    filename = 12345
    with pytest.raises(ValueError):
        task_func(metrics, filename)
    
    # Test case 4: Invalid input (log_dir does not exist)
    metrics = {'accuracy': 0.9, 'loss': 0.05}
    filename = 'metrics.txt'
    log_dir = 'invalid_log_dir'
    with pytest.raises(FileNotFoundError):
        task_func(metrics, filename, log_dir)
    
    # Test case 5: Invalid input (log_dir is not a directory)
    metrics = {'accuracy': 0.9, 'loss': 0.05}
    filename = 'metrics.txt'
    log_dir = 'README.md'
    with pytest.raises(NotADirectoryError):
        task_func(metrics, filename, log_dir)