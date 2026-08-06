import pandas as pd
import numpy as np
import pytest
from src_0701 import task_func

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    expected_result = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    
    df = pd.DataFrame(data, columns=cols)
    df_np = np.array(df)
    df = pd.DataFrame(df_np, columns=cols)
    correlation_matrix = df.corr()
    
    assert np.array_equal(correlation_matrix, expected_result)