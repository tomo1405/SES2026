python
import pandas as pd
import numpy as np
import pytest

def task_func(data, cols):
    df = pd.DataFrame(data, columns=cols)
    
    df_np = np.array(df)
    df = pd.DataFrame(df_np, columns=cols)
    
    correlation_matrix = df.corr()
    return correlation_matrix

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['a', 'b', 'c']
    
    expected_result = pd.DataFrame([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]], columns=cols, index=cols)
    
    result = task_func(data, cols)
    
    assert result.equals(expected_result)