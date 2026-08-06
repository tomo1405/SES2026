python
import os
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

from src_0382 import task_func

def test_task_func_valid_file():
    # Test if the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(file_path='non_existent_file.csv')

def test_task_func_valid_target_column():
    # Test if the function raises a ValueError if the target column does not exist in the CSV file
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df=df, target_column='non_existent_column')

def test_task_func_valid_data():
    # Test if the function returns a valid plot and feature importances for a valid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [0, 1, 0]})
    ax, importances = task_func(df=df, target_column='target')
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, pd.Series)
    assert len(importances) == 2

def test_task_func_valid_seed():
    # Test if the function returns the same plot and feature importances for the same seed
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [0, 1, 0]})
    ax1, importances1 = task_func(df=df, target_column='target', seed=42)
    ax2, importances2 = task_func(df=df, target_column='target', seed=42)
    assert ax1.get_title() == ax2.get_title()
    assert importances1.equals(importances2)