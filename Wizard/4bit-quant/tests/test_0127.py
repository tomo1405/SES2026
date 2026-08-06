python
import pandas as pd
import random
import statistics
import numpy as np
import pytest

from src_0127 import task_func

def test_task_func():
    # Test case 1: Test with default animals and seed
    report_df = task_func()
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df.iloc[0]['Animal'] == 'Lion'
    assert report_df.iloc[0]['Mean'] == 42.5
    assert report_df.iloc[0]['Median'] == 42
    assert report_df.iloc[0]['Mode'] == 42
    assert report_df.iloc[0]['Standard Deviation'] == 14.142135623730951
    
    # Test case 2: Test with custom animals and seed
    animals = ['Dog', 'Cat', 'Bird']
    seed = 10
    report_df = task_func(animals, seed)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (3, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df.iloc[0]['Animal'] == 'Dog'
    assert report_df.iloc[0]['Mean'] == 37.5
    assert report_df.iloc[0]['Median'] == 37
    assert report_df.iloc[0]['Mode'] == 37
    assert report_df.iloc[0]['Standard Deviation'] == 14.142135623730951
    
    # Test case 3: Test with invalid animals argument
    with pytest.raises(TypeError):
        task_func(123)
    
    # Test case 4: Test with invalid seed argument
    with pytest.raises(TypeError):
        task_func(seed='abc')