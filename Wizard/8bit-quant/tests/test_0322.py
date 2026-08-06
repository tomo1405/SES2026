python
import pandas as pd
import re
from scipy import stats
import pytest

def task_func(text):
    # Extracting names from the text
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    names = [name.strip() for name in names if name.strip()]  # Removing any empty or whitespace names

    # Counting name frequencies
    name_freqs = pd.Series(names).value_counts()
    
    # Creating a bar chart of name frequencies if there are names found
    if not name_freqs.empty:
        ax = name_freqs.plot(kind='bar', title="Name Frequencies")
        skewness = stats.skew(name_freqs)
        kurtosis = stats.kurtosis(name_freqs)
    else:
        ax = skewness = kurtosis = None

    if skewness == float('nan'):
        skewness = None
    if kurtosis == float('nan'):
        kurtosis = None
    
    return name_freqs, ax, skewness, kurtosis

def test_task_func():
    # Test case 1: Valid input
    text = "John [Smith] Doe, Jane [Doe-Smith], John [Doe]"
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.shape[0] == 2
    assert name_freqs.index.tolist() == ['John [Smith] Doe', 'Jane [Doe-Smith]']
    assert name_freqs.tolist() == [1, 1]
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 2: Empty input
    text = ""
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

    # Test case 3: Invalid input
    text = "John [Smith] Doe, Jane [Doe-Smith], John [Doe], "
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.shape[0] == 2
    assert name_freqs.index.tolist() == ['John [Smith] Doe', 'Jane [Doe-Smith]']
    assert name_freqs.tolist() == [1, 1]
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None