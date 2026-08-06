python
import pandas as pd
import pytest
from src_0430 import task_func
import seaborn as sns

@pytest.fixture
def data():
    df1 = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5], "feature1": [1, 2, 3, 4, 5], "feature2": [5, 4, 3, 2, 1]}
    )
    df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "target": [0, 1, 0, 1, 0]})
    return df1, df2

def test_task_func(data):
    df1, df2 = data
    selected_features, heatmap = task_func(df1, df2)
    assert selected_features == ["feature1", "feature2"]
    assert isinstance(heatmap, sns.matrix.ClusterGrid)