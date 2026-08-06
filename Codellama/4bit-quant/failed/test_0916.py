import pytest
from src_0916 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def test_task_func():
    # Test case 1: No outliers
    df = pd.DataFrame({'closing_price': [10, 11, 12, 13, 14, 15]})
    outliers, ax = task_func(df)
    assert outliers.empty
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend() == 'best'
    assert ax.get_lines()[0].get_color() == 'blue'
    assert ax.get_lines()[0].get_label() == 'Normal'
    assert ax.get_lines()[1].get_linestyle() == 'none'
    assert ax.get_lines()[1].get_marker() == 'X'
    assert ax.get_lines()[1].get_color() == 'red'
    assert ax.get_lines()[1].get_markersize() == 12
    assert ax.get_lines()[1].get_label() == 'Outlier'

    # Test case 2: With outliers
    df = pd.DataFrame({'closing_price': [10, 11, 12, 13, 14, 15, 1000]})
    outliers, ax = task_func(df)
    assert not outliers.empty
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend() == 'best'
    assert ax.get_lines()[0].get_color() == 'blue'
    assert ax.get_lines()[0].get_label() == 'Normal'
    assert ax.get_lines()[1].get_linestyle() == 'none'
    assert ax.get_lines()[1].get_marker() == 'X'
    assert ax.get_lines()[1].get_color() == 'red'
    assert ax.get_lines()[1].get_markersize() == 12
    assert ax.get_lines()[1].get_label() == 'Outlier'

    # Test case 3: Custom Z-score threshold
    df = pd.DataFrame({'closing_price': [10, 11, 12, 13, 14, 15, 1000]})
    outliers, ax = task_func(df, z_threshold=3)
    assert not outliers.empty
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend() == 'best'
    assert ax.get_lines()[0].get_color() == 'blue'
    assert ax.get_lines()[0].get_label() == 'Normal'
    assert ax.get_lines()[1].get_linestyle() == 'none'
    assert ax.get_lines()[1].get_marker() == 'X'
    assert ax.get_lines()[1].get_color() == 'red'
    assert ax.get_lines()[1].get_markersize() == 12
    assert ax.get_lines()[1].get_label() == 'Outlier'