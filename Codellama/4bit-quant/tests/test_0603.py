import os

import numpy as np
import pandas as pd
from src_0603 import task_func


def test_task_func():
    file_path = 'test_file.txt'
    output_dir = './output'
    task_func(file_path, output_dir)
    assert os.path.exists(output_dir)
    assert os.path.exists(file_path)
    matrix = pd.read_csv(file_path, sep='\t', header=None, index_col=None)
    assert matrix.shape == (10, 10)
    assert np.all(matrix.values == np.random.choice(LETTERS, (10, 10)))
    os.remove(file_path)
    os.rmdir(output_dir)