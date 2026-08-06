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

def test_task_func_valid_input():
    metrics = {'accuracy': 0.95, 'loss': 0.05}
    filename = 'metrics.txt'
    assert task_func(metrics, filename) == True

def test_task_func_invalid_input():
    metrics = 'not a dictionary'
    filename = 12345
    with pytest.raises(ValueError):
        task_func(metrics, filename)

def test_task_func_invalid_filename():
    metrics = {'accuracy': 0.95, 'loss': 0.05}
    filename = 'invalid/filename.txt'
    with pytest.raises(FileNotFoundError):
        task_func(metrics, filename)