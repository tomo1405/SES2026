import pytest
from src_0654 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mocking the plt.show() function to prevent GUI display during testing
@pytest.fixture(autouse=True)
def mock_plt_show(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)

def test_task_func_with_default_target_value():
    # Create a sample DataFrame
    data = io.StringIO("""
        A,B,C
        332,1,2
        4,332,5
        6,7,332
    """)
    df = pd.read_csv(data)

    # Call the function
    mask, ax = task_func(df)

    # Check if the mask is correct
    expected_mask = pd.DataFrame({
        'A': [True, False, False],
        'B': [False, True, False],
        'C': [False, False, True]
    })
    assert mask.equals(expected_mask), "The mask does not match the expected output."

def test_task_func_with_custom_target_value():
    # Create a sample DataFrame
    data = io.StringIO("""
        A,B,C
        100,1,2
        4,100,5
        6,7,100
    """)
    df = pd.read_csv(data)

    # Call the function with a custom target value
    mask, ax = task_func(df, target_value='100')

    # Check if the mask is correct
    expected_mask = pd.DataFrame({
        'A': [True, False, False],
        'B': [False, True, False],
        'C': [False, False, True]
    })
    assert mask.equals(expected_mask), "The mask does not match the expected output with the custom target value."

def test_task_func_with_no_match():
    # Create a sample DataFrame where no values match the target value
    data = io.StringIO("""
        A,B,C
        1,2,3
        4,5,6
        7,8,9
    """)
    df = pd.read_csv(data)

    # Call the function
    mask, ax = task_func(df)

    # Check if the mask is correct
    expected_mask = pd.DataFrame({
        'A': [False, False, False],
        'B': [False, False, False],
        'C': [False, False, False]
    })
    assert mask.equals(expected_mask), "The mask does not match the expected output when no values match the target value."