import pytest
from src_0487 import task_func

def test_task_func():
    start_time = 1000
    end_time = 2000
    step = 100
    trend = 0.5
    seed = 42

    ax = task_func(start_time, end_time, step, trend, seed)

    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Value"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Value"

    assert len(ax.get_xticks()) == 11
    assert ax.get_xticks()[0] == 1000
    assert ax.get_xticks()[-1] == 2000

    assert len(ax.get_yticks()) == 11
    assert ax.get_yticks()[0] == 0
    assert ax.get_yticks()[-1] == 1

    assert ax.get_xlim() == (1000, 2000)
    assert ax.get_ylim() == (0, 1)

    assert ax.get_title() == "Value vs Time"

def test_task_func_invalid_start_time():
    start_time = 2000
    end_time = 1000
    step = 100
    trend = 0.5
    seed = 42

    with pytest.raises(ValueError):
        task_func(start_time, end_time, step, trend, seed)

def test_task_func_invalid_step():
    start_time = 1000
    end_time = 2000
    step = 0
    trend = 0.5
    seed = 42

    with pytest.raises(ValueError):
        task_func(start_time, end_time, step, trend, seed)