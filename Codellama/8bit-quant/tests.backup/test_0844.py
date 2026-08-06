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

    # Test that the function returns the correct words in each sentence
    assert task_func(1).split(" ")[0] in WORD_LIST
    assert task_func(1).split(" ")[1] in WORD_LIST
    assert task_func(1).split(" ")[2] in WORD_LIST
    assert task_func(1).split(" ")[3] in WORD_LIST
    assert task_func(1).split(" ")[4] in WORD_LIST

    assert task_func(2).split(" ")[0] in WORD_LIST
    assert task_func(2).split(" ")[1] in WORD_LIST
    assert task_func(2).split(" ")[2] in WORD_LIST
    assert task_func(2).split(" ")[3] in WORD_LIST
    assert task_func(2).split(" ")[4] in WORD_LIST
    assert task_func(2).split(" ")[5] in WORD_LIST
    assert task_func(2).split(" ")[6] in WORD_LIST
    assert task_func(2).split(" ")[7] in WORD_LIST
    assert task_func(2).split(" ")[8] in WORD_LIST
    assert task_func(2).split(" ")[9] in WORD_LIST

    assert task_func(3).split(" ")[0] in WORD_LIST
    assert task_func(3).split(" ")[1] in WORD_LIST
    assert task_func(3).split(" ")[2] in WORD_LIST
    assert task_func(3).split(" ")[3] in WORD_LIST
    assert task_func(3).split(" ")[4] in WORD_LIST
    assert task_func(3).split(" ")[5] in WORD_LIST
    assert task_func(3).split(" ")[6] in WORD_LIST
    assert task_func(3).split(" ")[7] in WORD_LIST
    assert task_func(3).split(" ")[8] in WORD_LIST
    assert task_func(3).split(" ")[9] in WORD_LIST
    assert task_func(3).split(" ")[10] in WORD_LIST
    assert task_func(3).split(" ")[11] in WORD_LIST
    assert task_func(3).split(" ")[12] in WORD_LIST
    assert task_func(3).split(" ")[13] in WORD_LIST
    assert task_func(3).split(" ")[14] in WORD_LIST

    # Test that the function returns the correct number of periods
    assert task_func(1).count(".") == 1
    assert task_func(2).count(".") == 2
    assert task_func(3).count(".") == 3

    # Test that the function returns the correct number of spaces
    assert task_func(1).count(" ") == 4
    assert task_func(2).count(" ") == 9
    assert task_func(3).count(" ") == 14

    # Test that the function returns the correct number of words
    assert len(task_func(1).split(" ")) == 5
    assert len(task_func(2).split(" ")) == 10
    assert len(task_func(3).split(" ")) == 15

    # Test that the function returns the correct number of sentences
    assert len(task_func(1).split(".")) == 1
    assert len(task_func(2).split(".")) == 2
    assert len(task_func(3).split(".")) == 3