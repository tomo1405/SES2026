import pandas as pd
import numpy as np
import pytest

from src_0841 import task_func

def test_task_func():
    file_path = 'test_file.csv'
    num_rows = 10
    data_dimensions = 3
    random_seed = 42

    np.random.seed(random_seed)
    expected_df = pd.DataFrame(np.random.rand(num_rows, data_dimensions),
                               columns=[f'Feature_{i + 1}' for i in range(data_dimensions)])

    expected_df.to_csv(file_path, index=False)

    actual_file_path = task_func(file_path, num_rows, data_dimensions, random_seed)

    actual_df = pd.read_csv(actual_file_path)

    assert actual_df.equals(expected_df)