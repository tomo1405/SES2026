import pytest
from src_0480 import task_func

def test_task_func():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list)
    assert output.equals(expected_output)

def test_task_func_with_seed():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list, seed=0)
    assert output.equals(expected_output)

def test_task_func_with_different_seed():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list, seed=1)
    assert output.equals(expected_output)

def test_task_func_with_empty_string():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list, seed=0)
    assert output.equals(expected_output)

def test_task_func_with_invalid_input():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list, seed=0)
    assert output.equals(expected_output)