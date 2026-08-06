import statistics

import numpy as np
import pandas as pd
import pytest
from src_0127 import task_func


def test_task_func_default_animals():
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert len(result) == 5
    assert all(isinstance(row['Animal'], str) for row in result.to_dict('records'))

def test_task_func_custom_animals():
    custom_animals = ['Dog', 'Cat', 'Bird']
    result = task_func(custom_animals)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert len(result) == 3
    assert all(row['Animal'] in custom_animals for row in result.to_dict('records'))

def test_task_func_random_seed():
    result1 = task_func(seed=123)
    result2 = task_func(seed=123)
    pd.testing.assert_frame_equal(result1, result2)

def test_task_func_statistics():
    result = task_func()
    for index, row in result.iterrows():
        counts = [randint(1, 100) for _ in range(10)]
        assert row['Mean'] == statistics.mean(counts)
        assert row['Median'] == statistics.median(counts)
        try:
            assert row['Mode'] == statistics.mode(counts)
        except statistics.StatisticsError:
            # Mode can raise StatisticsError if there's no unique mode
            pass
        assert np.isclose(row['Standard Deviation'], np.std(counts))

def test_task_func_empty_animals():
    with pytest.raises(ValueError):
        task_func(animals=[])

def test_task_func_non_string_animals():
    with pytest.raises(TypeError):
        task_func(animals=[1, 2, 3])