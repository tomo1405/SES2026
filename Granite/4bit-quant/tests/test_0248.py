import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
from src_0248 import task_func
import pytest

N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def test_task_func():
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(N_DATA_POINTS)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    expected_df = pd.DataFrame(normalized_data, columns=['Normalized Value'])
    actual_df = task_func()

    assert actual_df.equals(expected_df)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(max_value=MIN_VALUE)