import pytest
from src_0048 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_df = pd.DataFrame({'A': [-1.22474487, -0.61237244, 0. ], 'B': [1.22474487, 1.83711731, 2.44948974]})
    expected_heatmap = <matplotlib.axes._axes.Axes object at 0x7f8e1d1d1d60>

    df_ returned, heatmap_returned = task_func(df)

    assert df_returned.equals(expected_df)
    assert heatmap_returned == expected_heatmap