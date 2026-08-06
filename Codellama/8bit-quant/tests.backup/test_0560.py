import pytest
from src_0560 import task_func
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def test_task_func():
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    expected_euclidean_distance = distance.euclidean(a, b)
    expected_df = pd.DataFrame({'A': a, 'B': b})
    expected_ax = plt.subplots()
    expected_ax.plot(expected_df['A'], expected_df['B'])
    expected_ax.plot([expected_df['A'].iloc[0], expected_df['B'].iloc[0]], [expected_df['A'].iloc[-1], expected_df['B'].iloc[-1]], 'ro-')

    euclidean_distance, df, ax = task_func(a, b)

    assert euclidean_distance == expected_euclidean_distance
    assert df.equals(expected_df)
    assert ax.get_figure() == expected_ax.get_figure()
    assert ax.get_axes() == expected_ax.get_axes()
    assert ax.get_lines() == expected_ax.get_lines()
    assert ax.get_legend() == expected_ax.get_legend()
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()