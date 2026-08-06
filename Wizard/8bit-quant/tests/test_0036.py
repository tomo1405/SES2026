python
import pytest
from src_0036 import task_func

def test_task_func():
    df = {'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7], 'col3': [5, 6, 7, 8, 9]}
    df = pd.DataFrame(df)
    target_values = [1, 3, 4]
    result, ax = task_func(df, target_values)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.Axes)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_title() == 'Density Plot of Selected Values'
    assert ax.get_legend().texts[0]._text == 'col1'
    assert ax.get_legend().texts[1]._text == 'col2'
    assert ax.get_legend().texts[2]._text == 'col3'
    assert ax.lines[0].get_xdata().tolist() == [1, 3, 4]
    assert ax.lines[0].get_ydata().tolist() == [0.1, 0.1, 0.1]
    assert ax.lines[1].get_xdata().tolist() == [1, 3, 4]
    assert ax.lines[1].get_ydata().tolist() == [0.1, 0.1, 0.1]
    assert ax.lines[2].get_xdata().tolist() == [1, 3, 4]
    assert ax.lines[2].get_ydata().tolist() == [0.1, 0.1, 0.1]