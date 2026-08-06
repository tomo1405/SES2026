import pytest
from src_0105 import task_func

def test_task_func():
    df = pd.DataFrame({'group': ['A', 'B', 'C', 'D', 'E'],
                       'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                       'value': [10, 20, 30, 40, 50]})
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Scatterplot of Values for Each Group Over Time'
    assert len(ax.get_lines()) == 5
    assert ax.get_lines()[0].get_color() == 'b'
    assert ax.get_lines()[1].get_color() == 'g'
    assert ax.get_lines()[2].get_color() == 'r'
    assert ax.get_lines()[3].get_color() == 'c'
    assert ax.get_lines()[4].get_color() == 'm'