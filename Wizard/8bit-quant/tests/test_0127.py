python
import pandas as pd
import random
import statistics
import numpy as np
import pytest

from src_0127 import task_func

def test_task_func():
    # Test with default arguments
    report_df = task_func()
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    assert all(isinstance(x, float) for x in report_df['Mean'].tolist())
    assert all(isinstance(x, float) for x in report_df['Median'].tolist())
    assert all(isinstance(x, float) for x in report_df['Mode'].tolist())
    assert all(isinstance(x, float) for x in report_df['Standard Deviation'].tolist())

    # Test with custom arguments
    animals = ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    seed = 42
    report_df = task_func(animals=animals, seed=seed)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    assert all(isinstance(x, float) for x in report_df['Mean'].tolist())
    assert all(isinstance(x, float) for x in report_df['Median'].tolist())
    assert all(isinstance(x, float) for x in report_df['Mode'].tolist())
    assert all(isinstance(x, float) for x in report_df['Standard Deviation'].tolist())

    # Test with invalid arguments
    with pytest.raises(TypeError):
        task_func(animals='Lion')
    with pytest.raises(TypeError):
        task_func(seed='42')
    with pytest.raises(ValueError):
        task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda', 'Mouse'])
    with pytest.raises(ValueError):
        task_func(seed=-42)