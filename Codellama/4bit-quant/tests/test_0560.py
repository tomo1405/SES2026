import pytest
from src_0560 import task_func
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def test_task_func():
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    expected_euclidean_distance = 2.23606797749979
    expected_df = pd.DataFrame({'A': a, 'B': b})
    expected_ax = plt.subplots()[1]
    expected_ax.plot(expected_df['A'], expected_df['B'])
    expected_ax.plot([expected_df['A'].iloc[0], expected_df['B'].iloc[0]], [expected_df['A'].iloc[-1], expected_df['B'].iloc[-1]], 'ro-')

    euclidean_distance, df, ax = task_func(a, b)

    assert euclidean_distance == expected_euclidean_distance
    assert df.equals(expected_df)
    assert ax.get_figure().canvas.get_renderer().get_text_width_height() == expected_ax.get_figure().canvas.get_renderer().get_text_width_height()