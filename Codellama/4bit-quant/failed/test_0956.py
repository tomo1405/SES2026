import pytest
from src_0956 import task_func

def test_task_func():
    # Test case 1: Empty text
    with pytest.raises(ValueError):
        task_func([], "")

    # Test case 2: Non-empty text
    text = "This is a test sentence."
    expected_words = ["This", "is", "a", "test", "sentence."]
    expected_frequencies = [1, 1, 1, 1, 1]
    expected_indices = np.arange(len(expected_words))

    ax = task_func(["test"], text)
    assert ax.get_xticks() == expected_indices
    assert ax.get_xticklabels() == expected_words
    assert ax.get_yticks() == expected_frequencies

    # Test case 3: Multiple words
    text = "This is a test sentence. This is another test sentence."
    expected_words = ["This", "is", "a", "test", "sentence.", "This", "is", "another", "test", "sentence."]
    expected_frequencies = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    expected_indices = np.arange(len(expected_words))

    ax = task_func(["test", "another"], text)
    assert ax.get_xticks() == expected_indices
    assert ax.get_xticklabels() == expected_words
    assert ax.get_yticks() == expected_frequencies

    # Test case 4: Custom replacement
    text = "This is a test sentence."
    expected_words = ["This", "is", "a", "test", "sentence."]
    expected_frequencies = [1, 1, 1, 1, 1]
    expected_indices = np.arange(len(expected_words))

    ax = task_func(["test"], text, replacement="_")
    assert ax.get_xticks() == expected_indices
    assert ax.get_xticklabels() == expected_words
    assert ax.get_yticks() == expected_frequencies