import pandas as pd
from src_0048 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df, heatmap = task_func(df)
    assert df.equals(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}))
    assert isinstance(heatmap, sns.heatmap)
    assert heatmap.get_label() == 'Correlation Matrix'
    assert heatmap.get_title() == 'Correlation Matrix'
    assert heatmap.get_xlabel() == 'Feature'
    assert heatmap.get_ylabel() == 'Feature'
    assert heatmap.get_cmap() == 'coolwarm'
    assert heatmap.get_annot() == True