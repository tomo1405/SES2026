import matplotlib.pyplot as plt
import pandas as pd
from src_0239 import task_func


def test_task_func():
    # Test 1: Check if the function returns a tuple with two elements
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]})
    result, ax = task_func(df)
    assert isinstance(result, tuple) and len(result) == 2

    # Test 2: Check if the function returns a DataFrame with the correct columns
    assert isinstance(result[0], pd.DataFrame) and set(result[0].columns) == {'Name', 'Age', 'Score'}

    # Test 3: Check if the function returns a matplotlib Axes object
    assert isinstance(result[1], plt.Axes)

    # Test 4: Check if the function plots the correct data
    assert result[1].get_xlabel() == 'Age (standardized)'
    assert result[1].get_ylabel() == 'Score (standardized)'
    assert result[1].get_title() == 'Scatter Plot of Standardized Age and Score'
    assert result[1].get_xlim() == (0, 1)
    assert result[1].get_ylim() == (0, 1)