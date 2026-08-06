import pytest
from src_0087 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    seed = 42
    df, ax = task_func(students=students, seed=seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, np.ndarray)
    assert df.shape == (len(students), 2)
    assert ax.shape == (1,)
    assert df.columns.tolist() == ["Student", "Score"]
    assert df["Student"].tolist() == students
    assert df["Score"].dtype == np.int64
    assert ax[0].get_ylabel() == "Score"