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
    text = "This is a test text with one name: [John Doe]."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 1
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 3: Multiple names found
    text = "This is a test text with multiple names: [John Doe], [Jane Doe], [Bob Smith]."
    name_freqs, ax, skewness, kurtosis = task_func(text)
    assert name_freqs.size == 3
    assert ax is not None
    assert skewness is not None
    assert kurtosis is not None

    # Test case 4: Invalid input
    text = "This is a test text with invalid input: [John Doe] [Jane Doe] [Bob Smith]."
    with pytest.raises(ValueError):
        task_func(text)