import pytest
from src_0916 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
    
    # Test with default Z-score threshold
    outliers, ax = task_func(df)
    assert np.allclose(outliers['closing_price'], [100])
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend()[0].get_text() == 'Normal'
    assert ax.get_legend()[1].get_text() == 'Outlier'
    
    # Test with custom Z-score threshold
    outliers, ax = task_func(df, z_threshold=3)
    assert np.allclose(outliers['closing_price'], [100])
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend()[0].get_text() == 'Normal'
    assert ax.get_legend()[1].get_text() == 'Outlier'
    
    # Test with no outliers
    df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
    outliers, ax = task_func(df, z_threshold=3)
    assert np.allclose(outliers['closing_price'], [])
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    assert ax.get_legend()[0].get_text() == 'Normal'
    assert ax.get_legend()[1].get_text() == 'Outlier'