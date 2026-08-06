import pytest
from src_1056 import task_func

def test_task_func():
    colors = ["Red", "Blue", "Green"]
    states = ["CA", "NY", "TX"]

    # Expected output based on the fixed seed
    expected_data = {
        "Color:State 1": ["Red:CA", "Green:NY"],
        "Color:State 2": ["Blue:TX"]
    }
    expected_df = pd.DataFrame(expected_data)

    # Run the function
    result_df = task_func(colors, states)

    # Check if the resulting DataFrame matches the expected DataFrame
    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_with_one_element():
    colors = ["Red"]
    states = ["CA"]

    # Expected output
    expected_data = {
        "Color:State 1": ["Red:CA"]
    }
    expected_df = pd.DataFrame(expected_data)

    # Run the function
    result_df = task_func(colors, states)

    # Check if the resulting DataFrame matches the expected DataFrame
    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_with_empty_lists():
    colors = []
    states = []

    # Expected output
    expected_df = pd.DataFrame()

    # Run the function
    result_df = task_func(colors, states)

    # Check if the resulting DataFrame matches the expected DataFrame
    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_with_more_colors_than_states():
    colors = ["Red", "Blue", "Green"]
    states = ["CA", "NY"]

    # Expected output based on the fixed seed
    expected_data = {
        "Color:State 1": ["Red:CA", "Blue:NY"],
        "Color:State 2": ["Green"]
    }
    expected_df = pd.DataFrame(expected_data)

    # Run the function
    result_df = task_func(colors, states)

    # Check if the resulting DataFrame matches the expected DataFrame
    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."

def test_task_func_with_more_states_than_colors():
    colors = ["Red", "Blue"]
    states = ["CA", "NY", "TX"]

    # Expected output based on the fixed seed
    expected_data = {
        "Color:State 1": ["Red:CA", "Blue:NY"],
        "Color:State 2": ["Red:TX"]
    }
    expected_df = pd.DataFrame(expected_data)

    # Run the function
    result_df = task_func(colors, states)

    # Check if the resulting DataFrame matches the expected DataFrame
    assert result_df.equals(expected_df), "The DataFrame does not match the expected output."