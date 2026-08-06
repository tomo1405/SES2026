import pandas as pd
import seaborn as sns
from src_0044 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    description, plots = task_func(df)
    assert isinstance(description, pd.DataFrame)
    assert isinstance(plots, list)
    assert len(plots) == 2
    for plot in plots:
        assert isinstance(plot, sns.displot)