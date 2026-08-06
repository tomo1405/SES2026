import pytest
from src_0368 import task_func

def test_task_func():
    activities = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
    ax = task_func(activities)
    assert ax.get_xlabel() == 'Day of the Week'
    assert ax.get_ylabel() == 'Number of Activities'
    assert ax.get_title() == 'Weekly Activity'
    assert ax.get_xticks() == ['Monday', 'Tuesday', 'Wednesday']
    assert ax.get_yticks() == [1, 2, 3]

def test_task_func_invalid_input():
    activities = [1, 2, 3]
    with pytest.raises(TypeError):
        task_func(activities)