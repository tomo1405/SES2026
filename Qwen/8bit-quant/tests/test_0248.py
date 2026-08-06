import random

import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0248 import task_func


def test_task_func_default_values():
    result = task_func()
    assert len(result) == 5000
    assert 'Normalized Value' in result.columns

def test_task_func_custom_values():
    n_data_points = 1000
    min_value = 5.0
    max_value = 15.0
    result = task_func(n_data_points, min_value, max_value)
    assert len(result) == n_data_points
    assert 'Normalized Value' in result.columns

def test_task_func_min_greater_than_max():
    with pytest.raises(ValueError):
        task_func(min_value=10.0, max_value=5.0)

def test_task_func_normalized_values():
    result = task_func()
    scaler = StandardScaler()
    original_data = [round(random.uniform(0.0, 10.0), 3) for _ in range(5000)]
    original_df = pd.DataFrame(original_data, columns=['Value'])
    expected_normalized_data = scaler.fit_transform(original_df[['Value']])
    expected_result = pd.DataFrame(expected_normalized_data, columns=['Normalized Value'])
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_result.reset_index(drop=True))

def test_task_func_data_distribution():
    result = task_func()
    assert result['Normalized Value'].mean() == pytest.approx(0.0, abs=0.1)
    assert result['Normalized Value'].std() == pytest.approx(1.0, abs=0.1)