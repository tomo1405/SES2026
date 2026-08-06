python
import string
import matplotlib.pyplot as plt
import pytest

def task_func(s):

    if not isinstance(s, str):
        raise TypeError("Expected string input")

    LETTERS = string.ascii_lowercase

    s = s.lower()

    letter_counts = {letter: s.count(letter) for letter in LETTERS}

    fig, ax = plt.subplots()
    ax.bar(letter_counts.keys(), letter_counts.values())
    ax.set_xlabel("Letters")
    ax.set_ylabel("Frequency")
    ax.set_title("Letter Frequencies")

    return letter_counts, ax

def test_task_func():
    # Test case 1: Valid input
    s = "Hello, World!"
    expected_letter_counts = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    expected_ax_title = "Letter Frequencies"
    letter_counts, ax = task_func(s)
    assert letter_counts == expected_letter_counts
    assert ax.get_title() == expected_ax_title

    # Test case 2: Invalid input (not a string)
    s = 12345
    with pytest.raises(TypeError):
        task_func(s)