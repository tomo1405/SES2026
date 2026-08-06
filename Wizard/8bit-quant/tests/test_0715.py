python
import sys
from pathlib import Path
import pytest

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Creating the directory if it does not exist
    Path(path_to_append).mkdir(parents=True, exist_ok=True)
    
    # Adding the directory to sys.path
    sys.path.append(path_to_append)
    
    return path_to_append

def test_task_func():
    # Test case 1: Default path_to_append
    assert task_func() == '/path/to/whatever'
    
    # Test case 2: Custom path_to_append
    assert task_func('/custom/path') == '/custom/path'
    
    # Test case 3: Path already exists
    Path('/custom/path').mkdir(parents=True, exist_ok=True)
    with pytest.raises(FileExistsError):
        task_func('/custom/path')