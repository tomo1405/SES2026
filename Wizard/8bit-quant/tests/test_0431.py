python
import pandas as pd
import pytest
from src_0431 import task_func

def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    labels, ax = task_func(df1, df2)
    assert len(labels) == 3
    assert ax.get_xlabel() == "feature1"
    assert ax.get_ylabel() == "feature2"