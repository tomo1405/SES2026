import pytest
from src_0526 import task_func

def test_task_func():
    input_file = "test_data.json"
    result, plots = task_func(input_file)
    assert isinstance(result, dict)
    assert isinstance(plots, list)
    assert len(plots) == len(result)
    for key, values in result.items():
        assert isinstance(values, dict)
        assert "mean" in values
        assert "median" in values
        assert isinstance(values["mean"], float)
        assert isinstance(values["median"], float)
    for plot in plots:
        assert isinstance(plot, matplotlib.axes.Axes)
        assert plot.get_title() == f"Statistics of {key}"
        assert plot.get_xlabel() == "mean"
        assert plot.get_ylabel() == "median"
        assert len(plot.get_xticks()) == 2
        assert len(plot.get_yticks()) == 2