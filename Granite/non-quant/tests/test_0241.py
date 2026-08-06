import pandas as pd
from random import uniform
from src_0241 import task_func
import pytest

def test_task_func():
    n_data_points = 1000
    min_value = 0.0
    max_value = 10.0
    column_name = 'Value'

    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    expected_df = pd.DataFrame(data, columns=[column_name])

    actual_df = task_func(n_data_points, min_value, max_value, column_name)

    assert actual_df.equals(expected_df)