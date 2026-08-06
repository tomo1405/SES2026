import pandas as pd
from src_0431 import task_func


def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature1": [10, 20, 30], "feature2": [100, 200, 300]})
    labels, ax = task_func(df1, df2)
    assert labels.shape == (3,)
    assert ax.shape == (3, 2)
    assert ax.xlabel == "feature1"
    assert ax.ylabel == "feature2"