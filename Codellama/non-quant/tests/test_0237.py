import pandas as pd
import pytest
from src_0237 import task_func


def test_task_func_input_type():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70], 'Category': ['A', 'B', 'C']})
    test_size = 0.2
    random_state = 42

    with pytest.raises(ValueError):
        task_func(df, test_size, random_state)

def test_task_func_output_type():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70], 'Category': ['A', 'B', 'C']})
    test_size = 0.2
    random_state = 42

    accuracy = task_func(df, test_size, random_state)

    assert isinstance(accuracy, float)

def test_task_func_output_value():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70], 'Category': ['A', 'B', 'C']})
    test_size = 0.2
    random_state = 42

    accuracy = task_func(df, test_size, random_state)

    assert accuracy > 0.5