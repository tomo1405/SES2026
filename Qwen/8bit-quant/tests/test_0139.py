import pytest
from src_0139 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mocking plt.show to prevent GUI display during tests
plt.show = lambda: None

def test_task_func_invalid_input():
    # Test with non-DataFrame input
    with pytest.raises(ValueError):
        task_func("not a dataframe")

    # Test with DataFrame missing 'Letters' column
    df_missing_column = pd.DataFrame({'Numbers': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df_missing_column)

def test_task_func_valid_input():
    # Test with valid DataFrame
    data = {'Letters': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(data)
    ax = task_func(df)

    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Letter Frequency'
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'

    # Check if the frequency counts are correct
    letter_frequency = df['Letters'].value_counts().reindex(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), fill_value=0)
    bars = [bar.get_height() for bar in ax.patches]
    assert bars == list(letter_frequency)

def test_task_func_empty_dataframe():
    # Test with empty DataFrame
    df_empty = pd.DataFrame(columns=['Letters'])
    ax = task_func(df_empty)

    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Letter Frequency'
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'

    # Check if all frequencies are zero
    bars = [bar.get_height() for bar in ax.patches]
    assert bars == [0] * 26

def test_task_func_custom_letters():
    # Test with custom letters
    data = {'Letters': ['X', 'Y', 'Z', 'X', 'Y']}
    df = pd.DataFrame(data)
    custom_letters = ['X', 'Y', 'Z']
    ax = task_func(df, letters=custom_letters)

    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Letter Frequency'
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'

    # Check if the frequency counts are correct for custom letters
    letter_frequency = df['Letters'].value_counts().reindex(custom_letters, fill_value=0)
    bars = [bar.get_height() for bar in ax.patches]
    assert bars == list(letter_frequency)