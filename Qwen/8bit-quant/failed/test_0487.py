import pytest
from src_0487 import task_func

def test_task_func_start_time_before_end_time():
    with pytest.raises(ValueError):
        task_func(1633072800000, 1633072800000, 60000, 0.1)

def test_task_func_invalid_step_value():
    with pytest.raises(ValueError):
        task_func(1633072800000, 1633076400000, 0, 0.1)

def test_task_func_valid_input():
    ax = task_func(1633072800000, 1633076400000, 60000, 0.1)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    df = ax.get_lines()[0].get_data()
    assert len(df[0]) == 7
    assert len(df[1]) == 7

def test_task_func_no_trend():
    ax = task_func(1633072800000, 1633076400000, 60000, 0)
    df = ax.get_lines()[0].get_data()
    assert np.allclose(df[1], df[1][0])

def test_task_func_positive_trend():
    ax = task_func(1633072800000, 1633076400000, 60000, 0.1)
    df = ax.get_lines()[0].get_data()
    assert df[1][-1] > df[1][0]

def test_task_func_negative_trend():
    ax = task_func(1633072800000, 1633076400000, 60000, -0.1)
    df = ax.get_lines()[0].get_data()
    assert df[1][-1] < df[1][0]