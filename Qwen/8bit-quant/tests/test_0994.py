import matplotlib.pyplot as plt
from src_0994 import task_func


def test_task_func_with_empty_string():
    ax = task_func("")
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0  # No lines (KDE plot) should be added
    assert len(ax.patches) == 0  # No patches (histogram bars) should be added

def test_task_func_with_single_word():
    ax = task_func("hello")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1  # One histogram bar for the word "hello"
    assert len(ax.lines) == 0  # No lines (KDE plot) should be added

def test_task_func_with_multiple_words():
    ax = task_func("hello world this is a test")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 1  # Multiple histogram bars for different words
    assert len(ax.lines) == 1  # One line (KDE plot) should be added

def test_task_func_with_punctuation():
    ax = task_func("hello, world! this is a test.")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 1  # Multiple histogram bars for different words
    assert len(ax.lines) == 1  # One line (KDE plot) should be added

def test_task_func_with_identical_words():
    ax = task_func("hello hello hello")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1  # One histogram bar for the word "hello"
    assert len(ax.lines) == 1  # One line (KDE plot) should be added

def test_task_func_with_single_character():
    ax = task_func("a b c d e")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5  # Five histogram bars for each character
    assert len(ax.lines) == 1  # One line (KDE plot) should be added

def test_task_func_with_variance_zero():
    ax = task_func("aaaaa aaaaa aaaaa")
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1  # One histogram bar for the word "aaaaa"
    assert len(ax.lines) == 0  # No lines (KDE plot) should be added due to zero variance

def test_task_func_with_singular_matrix_error():
    # This test case is more about ensuring that the exception is handled
    # rather than checking the plot output.
    ax = task_func("1 2 3 4 5 6 7 8 9 10")
    assert isinstance(ax, plt.Axes)
    # We cannot easily predict the number of patches or lines here,
    # but we can check that the plot object is created.