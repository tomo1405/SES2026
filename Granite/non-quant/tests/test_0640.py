import pandas as pd
import seaborn as sns
from src_0640 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert df.shape == (100, 5)
    assert len(ax.patches) == 25