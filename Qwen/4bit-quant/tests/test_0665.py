import pytest
from src_0665 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_sales_data():
    data = u"""Month,A,B,C
Jan,100,150,200
Feb,120,170,220
Mar,130,180,230"""
    return pd.read_csv(io.StringIO(data))

def test_task_func(sample_sales_data):
    fig, ax = plt.subplots()
    result_ax = task_func(sample_sales_data)

    assert result_ax == ax, "The function should return the same axes object that was passed in."

    # Check if the plot has the correct number of lines
    lines = ax.get_lines()
    assert len(lines) == 3, "There should be one line for each sales category (excluding 'Month')"

    # Check if the legend has the correct labels
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert set(legend_labels) == {'A', 'B', 'C'}, "The legend should have labels 'A', 'B', and 'C'"

    # Check if the x-ticks are set correctly
    xticks = ax.get_xticks()
    assert set(xticks) == {'Jan', 'Feb', 'Mar'}, "The x-ticks should match the months in the data"

    plt.close(fig)  # Close the figure to avoid memory leaks in tests