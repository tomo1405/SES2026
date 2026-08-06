import pytest
from src_0322 import task_func

def test_task_func():
    # Test case 1: No names found
    text = "This is a test text with no names."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.empty
    assert ax is None
    assert skewness is None
    assert kurtosis is None

    # Test case 2: One name found
    text = "This is a test text with one name: John."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 1
    assert name_freqs.index[0] == "John"
    assert name_freqs.values[0] == 1
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 3: Multiple names found
    text = "This is a test text with multiple names: John, Jane, Bob."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 3
    assert name_freqs.index[0] == "John"
    assert name_freqs.index[1] == "Jane"
    assert name_freqs.index[2] == "Bob"
    assert name_freqs.values[0] == 1
    assert name_freqs.values[1] == 1
    assert name_freqs.values[2] == 1
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 4: Names with brackets
    text = "This is a test text with names in brackets: [John], [Jane], [Bob]."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 3
    assert name_freqs.index[0] == "John"
    assert name_freqs.index[1] == "Jane"
    assert name_freqs.index[2] == "Bob"
    assert name_freqs.values[0] == 1
    assert name_freqs.values[1] == 1
    assert name_freqs.values[2] == 1
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 5: Names with brackets and whitespace
    text = "This is a test text with names in brackets and whitespace: [John], [Jane], [Bob]."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 3
    assert name_freqs.index[0] == "John"
    assert name_freqs.index[1] == "Jane"
    assert name_freqs.index[2] == "Bob"
    assert name_freqs.values[0] == 1
    assert name_freqs.values[1] == 1
    assert name_freqs.values[2] == 1
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None