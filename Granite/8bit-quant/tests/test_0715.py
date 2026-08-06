import sys
from pathlib import Path
from unittest.mock import patch


def task_func(path_to_append=PATH_TO_APPEND):
    # Creating the directory if it does not exist
    Path(path_to_append).mkdir(parents=True, exist_ok=True)
    
    # Adding the directory to sys.path
    sys.path.append(path_to_append)
    
    return path_to_append

def test_task_func():
    with patch('sys.path', []):
        assert task_func() == PATH_TO_APPEND
        assert PATH_TO_APPEND in sys.path