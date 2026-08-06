import pytest
from src_0560 import task_func
import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([1, 2, 3]), np.array([4, 5, 6])

def test_task_func_euclidean_distance(sample_data):
    a, b = sample_data
    euclidean_distance, _, _ = task_func(a, b)
    expected_distance = distance.euclidean(a, b)
    assert np.isclose(euclidean_distance, expected_distance)

def test_task_func_dataframe(sample_data):
    a, b = sample_data
    _, df, _ = task_func(a, b)
    expected_df = pd.DataFrame({'A': a, 'B': b})
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_plot(sample_data, mocker):
    a, b = sample_data
    _, _, ax = task_func(a, b)
    mocker.spy(ax, 'plot')
    assert ax.plot.call_count == 2
    ax.plot.assert_any_call(df['A'], df['B'])
    ax.plot.assert_any_call([df['A'].iloc[0], df['B'].iloc[0]], [df['A'].iloc[-1], df['B'].iloc[-1]], 'ro-')