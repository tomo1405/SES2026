python
import pytest
from src_0287 import task_func

def test_task_func():
    output_file = 'output.csv'
    test_directory = FILE_DIR
    total_words = task_func(output_file, test_directory)
    assert total_words == 1000000