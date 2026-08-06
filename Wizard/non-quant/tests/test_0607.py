python
import pandas as pd
import scipy.stats as stats
import pytest

def task_func(matrix):
    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    # Handle NaN values by replacing them with 0.0
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = [[-1.34164079, -0.4472136, 0.4472136],
                       [-0.4472136, 0.4472136, 1.34164079],
                       [0.4472136, 1.34164079, 2.23606798]]
    result = task_func(matrix)
    assert result.values.tolist() == expected_result