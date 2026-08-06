import pandas as pd
import time
import pytest
from src_0598 import task_func

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

# Sample data
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Charlie', 'Age': 35},
    {'Name': 'David', 'Age': 40},
    {'Name': 'Eve', 'Age': 45},
]

# Test case 1: Test the function with a valid letter
@pytest.mark.parametrize("letter", ['a', 'b', 'c'])
def test_valid_letter(letter):
    df = pd.DataFrame(data)
    filtered_df = task_func(df, letter)
    assert isinstance(filtered_df, pd.Series)
    assert len(filtered_df) > 0

# Test case 2: Test the function with an invalid letter
@pytest.mark.parametrize("letter", ['x', 'y', 'z', '1', '2', '3'])
def test_invalid_letter(letter):
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df, letter)

# Test case 3: Test the function with a letter that has no matching names
@pytest.mark.parametrize("letter", ['d', 'e', 'f'])
def test_no_matching_names(letter):
    df = pd.DataFrame(data)
    filtered_df = task_func(df, letter)
    assert isinstance(filtered_df, pd.Series)
    assert len(filtered_df) == 0

# Test case 4: Test the function with a large dataset
@pytest.mark.parametrize("letter", ['a', 'b', 'c'])
def test_large_dataset(letter):
    df = pd.DataFrame([{'Name': f'Name_{i}', 'Age': i} for i in range(100000)])
    start_time = time.time()
    filtered_df = task_func(df, letter)
    end_time = time.time()
    assert end_time - start_time < 1  # Ensure the function completes within 1 second