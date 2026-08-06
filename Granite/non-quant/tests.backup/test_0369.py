import os
import shutil
import random
import pytest
from src_0369 import task_func

def test_task_func():
    src_dir = "/path/to/source/directory"
    dest_dir = "/path/to/destination/directory"
    seed = 100
    file_name = task_func(src_dir, dest_dir, seed)
    assert file_name is not None
    src_file = os.path.join(src_dir, file_name)
    dest_file = os.path.join(dest_dir, file_name)
    assert os.path.exists(src_file) == False
    assert os.path.exists(dest_file) == True