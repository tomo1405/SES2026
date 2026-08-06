import pytest
from src_1056 import task_func

def test_task_func():
    colors = ["Red", "Green", "Blue"]
    states = ["CA", "NY", "TX"]

    expected_data = {
        "Color:State 1": ["Red:CA", "Blue:TX"],
        "Color:State 2": ["Green:NY"],
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = task_func(colors, states)

    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_single_element():
    colors = ["Red"]
    states = ["CA"]

    expected_data = {
        "Color:State 1": ["Red:CA"],
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = task_func(colors, states)

    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_more_colors_than_states():
    colors = ["Red", "Green", "Blue", "Yellow"]
    states = ["CA", "NY"]

    expected_data = {
        "Color:State 1": ["Red:CA", "Yellow:NY"],
        "Color:State 2": ["Green:CA", "Blue:NY"],
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = task_func(colors, states)

    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_more_states_than_colors():
    colors = ["Red", "Green"]
    states = ["CA", "NY", "TX", "FL"]

    expected_data = {
        "Color:State 1": ["Red:CA", "Green:TX"],
        "Color:State 2": ["Red:NY", "Green:FL"],
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = task_func(colors, states)

    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."