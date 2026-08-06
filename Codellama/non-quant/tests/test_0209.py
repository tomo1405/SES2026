import matplotlib
from src_0209 import task_func


def test_task_func():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert all(key in descriptive_stats for key in ['mean', 'std', 'min', '25%', '50%', '75%', '95%', 'max'])
    assert all(isinstance(value, float) for value in descriptive_stats.values())
    assert ax.get_title() == 'Random Walk'
    assert ax.get_xlabel() == 'Step'
    assert ax.get_ylabel() == 'Value'