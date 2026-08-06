import pandas as pd
import seaborn as sns
from src_0112 import task_func


def test_task_func():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Time': ['08:00', '09:00', '10:00'],
                       'Temperature': [20, 22, 24]})
    ax = task_func(df)
    assert isinstance(ax, sns.heatmap)
    assert ax.title.get_text() == 'Temperature Heatmap'
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Day'
    assert ax.get_zlabel() == 'Temperature'
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == [1, 2, 3]
    assert ax.get_zticks() == [20, 22, 24]