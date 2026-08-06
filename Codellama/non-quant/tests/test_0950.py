import numpy as np
import pandas as pd
from src_0950 import task_func


def test_task_func():
    rows = 5
    columns = 3
    seed = 1234
    expected_matrix = np.array([[0.5488135, 0.71518937, 0.60276335],
                              [0.4236548, 0.64589411, 0.83205029],
                              [0.88315636, 0.95717118, 0.87487336],
                              [0.891773, 0.52889496, 0.82156568],
                              [0.96366276, 0.58833287, 0.79172504]])
    expected_df = pd.DataFrame(expected_matrix)
    
    result = task_func(rows, columns, seed)
    
    assert np.allclose(result, expected_df)