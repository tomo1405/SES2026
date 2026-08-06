import pandas as pd
import seaborn as sns
from src_0640 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert len(df.index) == 100
    assert len(df.columns) == 5
    assert df.index[0] == 'Sample1'
    assert df.columns[0] == 'Feature1'
    assert ax.get_title() == 'Feature Correlation Matrix'