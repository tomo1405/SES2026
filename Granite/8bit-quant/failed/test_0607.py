import pandas as pd
from scipy import stats
import pytest

def task_func(matrix):
    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = [[-1.22474487, -1.15470054, -1.08465621],
                       [0.8660254, 0.95105652, 1.03608764],
                       [1.95105652, 2.03608764, 2.12111876]]
    result = task_func(matrix)
    assert result.values.tolist() == expected_result

def test_task_func_with_nan():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, np.nan]]
    expected_result = [[-1.22474487, -1.15470054, -1.08465621],
                       [0.8660254, 0.95105652, 1.03608764],
                       [1.95105652, 2.03608764, 0.0]]
    result = task_func(matrix)
    assert result.values.tolist() == expected_result