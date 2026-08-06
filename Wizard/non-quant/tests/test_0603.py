python
import os
import numpy as np
import pandas as pd
from src_0603 import task_func

def test_task_func():
    file_path = 'test.txt'
    output_dir = './output'
    task_func(file_path, output_dir)
    assert os.path.exists(os.path.join(output_dir, file_path))