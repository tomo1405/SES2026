import pytest
from src_0561 import task_func

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_multiple_years():
    with pytest.raises(ValueError):
        task_func("2020-01-01, 2021-01-01")

def test_task_func_valid_data():
    data = "2020-01-01, 2020-02-01, 2020-03-01"
    ax = task_func(data)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Month"
    assert ax.get_ylabel() == "Value"
    assert ax.get_title() == "Monthly Data for 2020"
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    plt.close(ax.get_figure())