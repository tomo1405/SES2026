import sys
from pathlib import Path
PATH_TO_APPEND = '/path/to/whatever'
def task_func(path_to_append=PATH_TO_APPEND):
    # Creating the directory if it does not exist
    Path(path_to_append).mkdir(parents=True, exist_ok=True)
    
    # Adding the directory to sys.path
    sys.path.append(path_to_append)
    
    return path_to_append
import pytest

def test_task_func():
    # Test case 1: Check if the directory is created
    path = task_func()
    assert Path(path).exists()
    
    # Test case 2: Check if the directory is added to sys.path
    assert path in sys.path