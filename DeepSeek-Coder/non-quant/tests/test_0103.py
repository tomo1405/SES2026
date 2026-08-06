import pytest
from src_0103 import task_func

def test_task_func():
    fig, df = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 10