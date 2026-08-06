import os

import matplotlib
from src_0594 import task_func


def test_task_func():
    hours = 10
    output_dir = './output'
    file_path, ax = task_func(hours, output_dir)
    assert os.path.exists(file_path)
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Vehicle Count'
    assert ax.get_title() == 'Traffic Data Over Time'
    assert len(ax.get_lines()) == len(VEHICLE_TYPES)
    assert all(line.get_label() in VEHICLE_TYPES for line in ax.get_lines())
    assert all(line.get_data()[0] == df['Time'] for line in ax.get_lines())
    assert all(line.get_data()[1] == df[VEHICLE_TYPES] for line in ax.get_lines())