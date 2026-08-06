import pytest
from src_0844 import task_func

def test_task_func():
    # Test that the function returns a string
    assert isinstance(task_func(1), str)

    # Test that the function returns the correct number of sentences
    assert len(task_func(1).split(".")) == 1
    assert len(task_func(2).split(".")) == 2
    assert len(task_func(3).split(".")) == 3

    # Test that the function returns the correct number of words in each sentence
    assert len(task_func(1).split(" ")) == 5
    assert len(task_func(2).split(" ")) == 10
    assert len(task_func(3).split(" ")) == 15

    # Test that the function returns the correct number of characters in each sentence
    assert len(task_func(1)) == 5
    assert len(task_func(2)) == 10
    assert len(task_func(3)) == 15

    # Test that the function returns the correct number of periods in each sentence
    assert task_func(1).count(".") == 1
    assert task_func(2).count(".") == 2
    assert task_func(3).count(".") == 3

    # Test that the function returns the correct number of spaces in each sentence
    assert task_func(1).count(" ") == 4
    assert task_func(2).count(" ") == 8
    assert task_func(3).count(" ") == 12

    # Test that the function returns the correct number of words in the entire text
    assert len(task_func(1).split(" ")) == 5
    assert len(task_func(2).split(" ")) == 10
    assert len(task_func(3).split(" ")) == 15

    # Test that the function returns the correct number of characters in the entire text
    assert len(task_func(1)) == 5
    assert len(task_func(2)) == 10
    assert len(task_func(3)) == 15

    # Test that the function returns the correct number of periods in the entire text
    assert task_func(1).count(".") == 1
    assert task_func(2).count(".") == 2
    assert task_func(3).count(".") == 3

    # Test that the function returns the correct number of spaces in the entire text
    assert task_func(1).count(" ") == 4
    assert task_func(2).count(" ") == 8
    assert task_func(3).count(" ") == 12