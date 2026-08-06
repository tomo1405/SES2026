import pytest
from src_1080 import task_func

def test_task_func():
    data = [["100", "200", "300"], ["400", "500", "600"]]
    expected_mean = 350.0
    expected_median = 350.0
    expected_std_dev = 170.71067811865475
    expected_ax_settings = (
        [4, 1, 1, 1, 1],
        [0.0, 175.0, 350.0, 525.0, 700.0],
        <matplotlib.axes._base.Axes object at 0x7f8e1d1d1d60>
    )

    result, ax = task_func(data)

    assert result["mean"] == expected_mean
    assert result["median"] == expected_median
    assert result["std_dev"] == expected_std_dev
    assert ax == expected_ax_settings