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
    # Test case 1
    s = "Hello World"
    expected_letter_counts = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    expected_ax_title = "Letter Frequencies"

    letter_counts, ax = task_func(s)

    assert letter_counts == expected_letter_counts
    assert ax.get_title() == expected_ax_title

    # Test case 2
    s = "Python is awesome"
    expected_letter_counts = {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1, 'i': 1, 's': 1, 'a': 1, 'w': 1, 'm': 1, 'e': 1}
    expected_ax_title = "Letter Frequencies"

    letter_counts, ax = task_func(s)

    assert letter_counts == expected_letter_counts
    assert ax.get_title() == expected_ax_title

    # Test case 3
    s = "12345"
    expected_error = TypeError("Expected string input")

    with pytest.raises(TypeError) as e:
        letter_counts, ax = task_func(s)

    assert str(e.value) == str(expected_error)