import pytest
from src_0226 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_basic():
    # Test with a simple DataFrame and dictionary
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 4: 40}
    result = task_func(df, dct)
    assert result.equals(pd.DataFrame({'A': [10, 2, 3], 'B': [40, 5, 6]}))

def test_task_func_with_plot():
    # Test with plotting histograms
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 4: 40}
    buf = BytesIO()
    plt.switch_backend('Agg')
    plt.ioff()
    with plt.rc_context({'figure.figsize': (8, 6)}):
        task_func(df, dct, columns=['A', 'B'], plot_histograms=True)
        plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert img_str.startswith('iVBORw0KGgoAAAANSUhEUgAA')

def test_task_func_non_dataframe_input():
    # Test with non-DataFrame input
    with pytest.raises(ValueError):
        task_func([1, 2, 3], {})

def test_task_func_no_columns_to_plot():
    # Test with no columns to plot
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 4: 40}
    result = task_func(df, dct, plot_histograms=True)
    assert result.equals(pd.DataFrame({'A': [10, 2, 3], 'B': [40, 5, 6]}))

def test_task_func_missing_column():
    # Test with a missing column in the DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {1: 10, 4: 40}
    result = task_func(df, dct, columns=['C'], plot_histograms=True)
    assert result.equals(pd.DataFrame({'A': [10, 2, 3], 'B': [40, 5, 6]}))