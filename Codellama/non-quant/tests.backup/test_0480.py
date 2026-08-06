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
        "",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    expected_output = [
        "",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi"
    ]
    output = task_func(data_list)
    assert output.equals(expected_output)

def test_task_func_with_single_string():
    data_list = [
        "apple, banana, cherry"
    ]
    expected_output = [
        "apple, banana, cherry"
    ]
    output = task_func(data_list)
    assert output.equals(expected_output)

def test_task_func_with_multiple_strings():
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

def test_task_func_with_duplicate_strings():
    data_list = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi",
        "apple, banana, cherry"
    ]
    expected_output = [
        "apple, banana, cherry",
        "orange, pear, grapes",
        "strawberry, watermelon, kiwi",
        "apple, banana, cherry"
    ]
    output = task_func(data_list)
    assert output.equals(expected_output)