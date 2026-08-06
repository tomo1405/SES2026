import pytest
from src_0322 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "Alice, Bob, Charlie"
    result = task_func(text)
    assert isinstance(result, tuple), "The result should be a tuple"
    name_freqs, ax, skewness, kurtosis = result
    assert isinstance(name_freqs, pd.Series), "name_freqs should be a pandas Series"
    assert ax is None, "ax should be None if no plot is created"
    assert skewness is None, "skewness should be None if no plot is created"
    assert kurtosis is None, "kurtosis should be None if no plot is created"

    # Test case 2: Text with names
    text = "Alice, Bob, Charlie, Alice"
    result = task_func(text)
    name_freqs, ax, skewness, kurtosis = result
    assert isinstance(name_freqs, pd.Series), "name_freqs should be a pandas Series"
    assert ax is not None, "ax should not be None if a plot is created"
    assert skewness is not None, "skewness should not be None if a plot is created"
    assert kurtosis is not None, "kurtosis should not be None if a plot is created"

    # Add more test cases as needed