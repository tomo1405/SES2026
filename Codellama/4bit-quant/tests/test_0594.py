import os

from src_0594 import task_func


def test_task_func():
    hours = 10
    output_dir = './output'
    FILE_PATH, ax = task_func(hours, output_dir)
    assert os.path.exists(FILE_PATH)
    assert ax is not None
    assert ax.get_title() == 'Traffic Data Over Time'
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Vehicle Count'
    assert len(ax.get_lines()) == len(VEHICLE_TYPES)
    assert len(ax.get_xticks()) == hours
    assert len(ax.get_yticks()) == len(VEHICLE_TYPES)
    plt.close(ax.get_figure())