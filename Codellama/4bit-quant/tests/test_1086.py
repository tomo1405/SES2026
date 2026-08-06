from src_1086 import task_func


def test_task_func():
    # Test with valid input
    text = "This is a sample text for testing"
    expected_words = ["this", "is", "a", "sample", "text", "for", "testing"]
    expected_counts = [1, 1, 1, 1, 1, 1, 1]
    expected_ax = [1, 1, 1, 1, 1, 1, 1]
    words, ax = task_func(text)
    assert words == expected_words
    assert ax == expected_ax

    # Test with invalid input
    text = "This is a sample text for testing"
    expected_words = []
    expected_counts = []
    expected_ax = []
    words, ax = task_func(text)
    assert words == expected_words
    assert ax == expected_ax

    # Test with empty input
    text = ""
    expected_words = []
    expected_counts = []
    expected_ax = []
    words, ax = task_func(text)
    assert words == expected_words
    assert ax == expected_ax