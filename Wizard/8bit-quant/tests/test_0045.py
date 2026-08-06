python
import pytest
from src_0045 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)