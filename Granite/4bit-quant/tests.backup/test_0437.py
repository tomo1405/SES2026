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
    with pytest.raises(TypeError):
        task_func(123)  # Test if TypeError is raised when input is not a string

    input_str = "Hello, World!"
    expected_letter_counts = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    expected_xlabel = "Letters"
    expected_ylabel = "Frequency"
    expected_title = "Letter Frequencies"

    letter_counts, ax = task_func(input_str)

    assert letter_counts == expected_letter_counts  # Test if letter_counts dictionary is correct
    assert ax.get_xlabel() == expected_xlabel  # Test if xlabel is set correctly
    assert ax.get_ylabel() == expected_ylabel  # Test if ylabel is set correctly
    assert ax.get_title() == expected_title  # Test if title is set correctly