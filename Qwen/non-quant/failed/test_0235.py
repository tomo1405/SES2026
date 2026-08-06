import pytest
from src_0235 import task_func
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import io
import sys

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [88, 92, 87, 88]
    }
    return pd.DataFrame(data)

def test_task_func_input_type(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df['Name'])

def test_task_func_drop_duplicates(sample_df):
    df = sample_df.copy()
    df.drop_duplicates(subset='Name', inplace=True)
    plt, ax = task_func(df)
    assert len(df) == len(ax.lines[0].get_xdata())

def test_task_func_linregress(sample_df):
    df = sample_df.copy()
    df.drop_duplicates(subset='Name', inplace=True)
    slope, intercept, _, _, _ = stats.linregress(df['Age'], df['Score'])
    plt, ax = task_func(df)
    assert ax.lines[1].get_xdata()[0] == df['Age'].min()
    assert ax.lines[1].get_ydata()[0] == intercept + slope * df['Age'].min()

def test_task_func_plot_labels(sample_df):
    plt, ax = task_func(sample_df)
    assert ax.get_xlabel() == 'Age'
    assert ax.get_ylabel() == 'Score'
    assert ax.get_title() == 'Linear Regression'
    assert ax.get_legend().get_texts()[0].get_text() == 'Data'
    assert ax.get_legend().get_texts()[1].get_text() == 'Fitted line'

def test_task_func_plot_output(sample_df):
    plt, ax = task_func(sample_df)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.read() != b''

def test_task_func_no_duplicates(sample_df):
    df = sample_df.drop_duplicates(subset='Name')
    plt, ax = task_func(df)
    assert len(df) == len(ax.lines[0].get_xdata())