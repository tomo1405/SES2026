import pytest
from src_0320 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    example_str = "This is a test. This test is only a test."
    ax, top_n_words = task_func(example_str=example_str)
    assert isinstance(ax, plt.Axes), "Expected ax to be a matplotlib Axes object"
    assert isinstance(top_n_words, dict), "Expected top_n_words to be a dictionary"
    assert len(top_n_words) <= 30, "Expected top_n to be at most 30"

    # Add more test cases as needed

# You can add more test cases to cover different scenarios