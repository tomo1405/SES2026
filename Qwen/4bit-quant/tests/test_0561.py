import pytest
from src_0561 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="The provided data string is empty."):
        task_func("")

def test_task_func_multiple_years():
    with pytest.raises(ValueError, match="The provided data contains entries from multiple years."):
        task_func("2020-01-10,2021-02-20")

def test_task_func_valid_data():
    result = task_func("2020-01-10,2020-02-20,2020-03-30")
    assert isinstance(result, plt.Axes)
    assert result.get_title() == "Monthly Data for 2020"

def test_task_func_single_entry():
    result = task_func("2020-01-10")
    assert isinstance(result, plt.Axes)
    assert result.get_title() == "Monthly Data for 2020"

def test_task_func_correct_dataframe():
    result = task_func("2020-01-10,2020-02-20,2020-03-30")
    df = pd.DataFrame([("January", 10), ("February", 20), ("March", 30)], columns=['Month', 'Value'])
    df = df.set_index('Month')
    pd.testing.assert_frame_equal(result.figure.axes[0].get_lines()[0].get_xdata(), df.index)
    pd.testing.assert_series_equal(result.figure.axes[0].get_lines()[0].get_ydata(), df['Value'])

def test_task_func_no_display():
    result = task_func("2020-01-10,2020-02-20,2020-03-30")
    assert result.figure.canvas.draw_idle() is None