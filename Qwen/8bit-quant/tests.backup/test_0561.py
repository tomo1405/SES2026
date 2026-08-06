import pytest
from src_0561 import task_func
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Mocking the matplotlib plt object to capture the plot creation
class MockPlot:
    def bar(self, x, y):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

    def set_title(self, title):
        pass

    def xticks(self, rotation):
        pass

plt.subplots = lambda figsize: (MockPlot(), MockPlot())

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="The provided data string is empty."):
        task_func("")

def test_task_func_multiple_years():
    with pytest.raises(ValueError, match="The provided data contains entries from multiple years."):
        task_func("2020-01-100,2021-02-200")

def test_task_func_valid_data():
    data = "2020-01-100,2020-02-200,2020-03-300"
    ax = task_func(data)
    assert isinstance(ax, MockPlot)

def test_task_func_dataframe_contents():
    data = "2020-01-100,2020-02-200,2020-03-300"
    ax = task_func(data)
    expected_df = pd.DataFrame({
        'Month': ['January', 'February', 'March'],
        'Value': [100, 200, 300]
    }).set_index('Month')
    assert ax.bar.call_args_list == [(expected_df.index, expected_df['Value'])]

def test_task_func_plot_labels():
    data = "2020-01-100,2020-02-200,2020-03-300"
    ax = task_func(data)
    assert ax.set_xlabel.call_args_list == [pytest.call('Month')]
    assert ax.set_ylabel.call_args_list == [pytest.call('Value')]
    assert ax.set_title.call_args_list == [pytest.call('Monthly Data for 2020')]
    assert ax.xticks.call_args_list == [pytest.call(rotation='vertical')]

def test_task_func_plot_size():
    data = "2020-01-100,2020-02-200,2020-03-300"
    fig, ax = plt.subplots(figsize=(10, 6))
    task_func(data)
    assert fig.get_size_inches() == (10, 6)