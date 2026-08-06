python
import pytest
from src_0048 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df, heatmap = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(heatmap, sns.matrix.ClusterGrid)