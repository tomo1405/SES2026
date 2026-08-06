import pytest
from src_0048 import task_func

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df, heatmap = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(heatmap, sns.heatmap)
    assert df.shape == (3, 3)
    assert heatmap.shape == (3, 3)
    assert heatmap.get_array().shape == (3, 3)
    assert heatmap.get_array().min() >= -1
    assert heatmap.get_array().max() <= 1