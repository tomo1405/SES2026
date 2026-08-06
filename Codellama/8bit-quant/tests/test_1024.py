import pytest
from src_1024 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_dataframe():
    dataframe = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(dataframe)

def test_task_func_non_numeric_columns():
    dataframe = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    with pytest.raises(TypeError):
        task_func(dataframe)

def test_task_func_single_column_dataframe():
    dataframe = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(dataframe)

def test_task_func_valid_dataframe():
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    task_func(dataframe)
    assert plt.gca().get_title() == "Scatter plot between A and B"
    assert plt.gca().get_xlabel() == "A"
    assert plt.gca().get_ylabel() == "B"
    assert plt.gca().get_xlim() == (1, 3)
    assert plt.gca().get_ylim() == (4, 6)
    plt.close()