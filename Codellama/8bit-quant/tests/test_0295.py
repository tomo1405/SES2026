import pytest
from src_0295 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [20, 25, 30, 35, 40, 45], 'income': [50000, 60000, 70000, 80000, 90000, 100000]})
    expected_output = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [0.0, 0.5, 1.0, 1.5, 2.0, 2.5], 'income': [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]})
    output = task_func(df)
    pd.testing.assert_frame_equal(output, expected_output)