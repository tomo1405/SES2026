import matplotlib
import pandas as pd
from src_0592 import task_func


def test_task_func():
    hours = 10
    file_path = 'custom_data.csv'
    file_path, ax = task_func(hours, file_path)

    assert isinstance(file_path, str)
    assert isinstance(ax, matplotlib.axes.Axes)

    df = pd.read_csv(file_path)
    assert len(df) == hours
    assert set(df['Category'].unique()) == set(TEMP_CATEGORIES)

    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Data Over Time')

    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Temperature'
    assert ax.get_title() == 'Temperature Data Over Time'