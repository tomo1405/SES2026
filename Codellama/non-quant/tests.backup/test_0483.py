import pytest
from src_0483 import task_func
import pandas as pd
import random
import re

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]
    seed = 1234
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]
    seed = 4321
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_different_operation():
    data_list = ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]
    seed = 1234
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_empty_list():
    data_list = []
    seed = 1234
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": []})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_single_element_list():
    data_list = ["apple, banana, cherry"]
    seed = 1234
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": ["apple, banana, cherry"]})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_multiple_elements_list():
    data_list = ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]
    seed = 1234
    expected_output = pd.DataFrame({"Original String": data_list, "Modified String": ["apple, banana, cherry", "orange, pear, grapes", "strawberry, watermelon, mango"]})
    output = task_func(data_list, seed)
    assert output.equals(expected_output)