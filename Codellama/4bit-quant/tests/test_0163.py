import pytest
from src_0163 import task_func

def test_task_func():
    # Test case 1: Empty string
    text = ""
    rwidth = 0.8
    ax = task_func(text, rwidth)
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 0)
    assert ax.get_ylim() == (0, 0)

    # Test case 2: Single word
    text = "hello"
    rwidth = 0.8
    ax = task_func(text, rwidth)
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 5)
    assert ax.get_ylim() == (0, 1)

    # Test case 3: Multiple words
    text = "hello world"
    rwidth = 0.8
    ax = task_func(text, rwidth)
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 2)

    # Test case 4: Non-default rwidth
    text = "hello world"
    rwidth = 0.5
    ax = task_func(text, rwidth)
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 2)

    # Test case 5: Non-default rwidth
    text = "hello world"
    rwidth = 1.5
    ax = task_func(text, rwidth)
    assert ax.get_title() == "Distribution of Word Lengths"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 2)