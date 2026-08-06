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
    cols = ['A', 'B', 'C']
    expected_result = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
    
    result = task_func(data, cols)
    
    assert np.array_equal(result, expected_result)

if __name__ == "__main__":
    pytest.main()