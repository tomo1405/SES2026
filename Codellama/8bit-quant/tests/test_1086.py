from src_1086 import task_func


def test_task_func():
    text = "This is a sample text for testing."
    expected_words = ["this", "is", "a", "sample", "text", "for", "testing"]
    expected_counts = [1, 1, 1, 1, 1, 1, 1]

    words, ax = task_func(text)

    assert words == expected_words
    assert ax.get_xlabel() == "Word"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Most Common Words"
    assert ax.get_xticks() == expected_words
    assert ax.get_yticks() == expected_counts