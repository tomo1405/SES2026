import pytest
from src_0592 import task_func

def test_task_func():
    hours = 10
    file_path = 'custom_data.csv'
    file_path, ax = task_func(hours, file_path)
    assert file_path == 'custom_data.csv'
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Temperature Data Over Time'
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Temperature'
    assert ax.get_legend() == 'Category'
    assert len(ax.get_legend().get_texts()) == 3
    assert ax.get_legend().get_texts()[0].get_text() == 'Cold'
    assert ax.get_legend().get_texts()[1].get_text() == 'Normal'
    assert ax.get_legend().get_texts()[2].get_text() == 'Hot'
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_label() == 'Cold'
    assert ax.get_lines()[1].get_label() == 'Normal'
    assert ax.get_lines()[2].get_label() == 'Hot'
    assert len(ax.get_lines()[0].get_data()) == hours
    assert len(ax.get_lines()[1].get_data()) == hours
    assert len(ax.get_lines()[2].get_data()) == hours
    assert ax.get_lines()[0].get_data()[0] == 0
    assert ax.get_lines()[1].get_data()[0] == 25
    assert ax.get_lines()[2].get_data()[0] == 40
    plt.close()